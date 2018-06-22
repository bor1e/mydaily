import mechanicalsoup
from datetime import date, datetime, timedelta
from bottle import template
from libs.tanach import tanach

class Parser():

    def __init__(self, user, books, speed):
       # self.user = user
        self.books = books
        self.speed = speed
        self.word_count_total = 0
        self.browser = mechanicalsoup.StatefulBrowser()

    def content(self, visitors):
        ''' 
        Iterate over each book, which was passed to the parser, and get its content. 
        The content is retrieved, based on its value in the sqlite DB.
        The value is either the article id (aid) or the date, for
        daily reading at chabad.org.
        '''
        content = ''
        for key, value in self.__dict__['books'].items():
            content += getattr(self, key)(value)

        head = template('templates/head', totaltime=int((self.word_count_total/self.speed)/60), visitors=visitors)
        return (head+content)

    # NOTE: 
    # all the books, need to have aquivalent functions, to dynamically 
    # (TODO: user-based) retrieve the required content 
    # date already in use -> date_
    def tora(self, date_=None):
        ''' 
        The torahreading includes, is date-based. Chabad.org provides for each date the
        aquivalent torahreading portion with Raschi's commentary. The Torahreading, 
        maybe devided by different chapters, which are stored in different tables.  
        '''
        if not date_:
            date_ = date.today().strftime("%m-%d-%Y")
        page = self._get_page('torahreading',date_)
        parasha = page.find('h3', class_="article-header__subtitle").text
        # narrow page to the root element, in which all the relevant content is stored
        page = page.find('root')
        chapters = page.find_all('h3')
        tables = page.find_all('table')
        content = ''
        word_count = 0
        
        week = {6:'Rishon',
                0:'Sheni',
                1:'Shlishi',
                2:'Rewi`i',
                3:'Chamischi',
                4:'Shishi',
                5:'Schabbat Kodesh'}
        weekday = datetime.strptime(date_, "%m-%d-%Y").weekday()
        alia = week[weekday]
    

        # iterate over each chapter, and get its psukim
        for chap in range(len(chapters)):
            content += '<p class="subtitle">' + str(chapters[chap].text) +'</p>'
            trs = tables[chap].find_all('tr')
            content, word_count = self._get_tanach_with_rashi_from_table_rows(content, word_count, trs, 'span')
            
        # NOTE: next reserved word -> next_
        previous, today, next_ = self._days_prev_today_next(date_) 
        category = 'tora'
        buttons = template('templates/buttons', link=category, next=next_, previous=previous, today=today)
        self.word_count_total += word_count
        return template('templates/book', content=content, attr=int((word_count/self.speed)/60), title=(parasha+' - '+alia), category=category, buttons=buttons)
   

    def hayomyom(self, date_=None):
        if not date_:
            date_ = date.today().strftime("%m-%d-%Y")
        page = self._get_page('hayomyom',date_)
        #hyy: hayomyom - paragrapgh
        hyy = page.find('div', class_="co_body article-body cf")
        hyy_date = hyy.find('tr', class_='hayom-yom-date')
        hyy_weekday = hyy_date.find_all('td')[0].text
        hyy_day = hyy_date.find_all('td')[1].text
        hyy_year = hyy_date.find_all('td')[2].text
        content = ''
        word_count = 0
        for p in hyy.find_all('p'):
            content += '<p>' + p.text +' </p>'
            word_count += len(p.text.split())

        previous, today, next_ = self._days_prev_today_next(date_) 
        category = 'hayomyom'
        buttons = template('templates/buttons', link=category, next=next_, previous=previous, today=today)
        self.word_count_total += word_count
        return template('templates/book', content=content, attr=int((word_count/self.speed)/60), title='HaYom Yom - '+hyy_day, category=category, buttons=buttons)

    def rambam(self, date_=None):
        if not date_:
            date_ = date.today().strftime("%m-%d-%Y")
        page = self._get_page('rambam', date_)
        title = page.find('h2', class_="rambam_h2").text
        halachot = page.find_all('div', class_="verse-wrapper linear")
        word_count = 0
        content = ''
        for verse in halachot:
            halacha_num = 0
            if verse.find('span', class_="versenum"):
                halacha_num = int(verse.find('span', class_="versenum").text)
            #remove(ignore)  hebrew text from verse paragraph
            hebrew_text = verse.find('span', class_="alternate_he")
            hebrew_text.extract()
            #remove(ignore) footnotes link from verse paragraph
            footnotes = verse.find_all('a', class_="footnote_ref")
            for footnote in footnotes:
                footnote.extract()
            #ps: paragraphs
            ps = verse.find_all('p')
            halacha = ''
            for p in ps:
                halacha += '<p>'+p.text+'</p>'
                word_count += len(p.text.split())
            content += template('templates/rambam_list', rule_num=halacha_num, rule=halacha)

        previous, today, next_ = self._days_prev_today_next(date_) 
        category = 'rambam'
        buttons = template('templates/buttons', link=category, next=next_, previous=previous, today=today)
        self.word_count_total += word_count
        return template('templates/book', content=content, attr=int((word_count/self.speed)/60), title=('Rambam - ' +title), category=category, buttons=buttons)


    def tanach(self, aid=None, book=None, chapter=None, url=None):
        if aid:
            url = 'https://www.chabad.org/library/bible.aspx?aid='+str(aid)
            self.browser.open(url)
            page = self.browser.get_current_page()
        elif book:
            #find aid and call the same function with aid of tanach
            page = self._get_tanach_aid_by_book(book, chapter)
        elif url:
            self.browser.open(url)
            page = self.browser.get_current_page()
        else:
            page = self._get_tanach_aid_by_book('Yehoshua - Joshua')

        title = page.find('h1').text
        table = page.find('table', class_='Co_TanachTable')
        content = ''
        word_count = 0
        trs = table.find_all('tr')
       
        content, word_count = self._get_tanach_with_rashi_from_table_rows(content, word_count, trs, 'a')
        next_ = aid+1
        previous = aid -1
        category = 'tanach'
        buttons = template('templates/buttons', link=category, next=next_, previous=previous, today=None)
        self.word_count_total += word_count
        return template('templates/book', content=content, attr=int((word_count/self.speed)/60), title=title,  category=category, buttons=buttons)

    # beginn of helper functions

    def _get_tanach_with_rashi_from_table_rows(self, content, word_count, trs, verse_num):
        '''
        Iterate over each table row, retrieve its verse number, 
        its verse context and its Rashi comment 
        '''
        i = 0
        while i<len(trs):
                tr = trs[i]
                passuk_num = int(tr.find(verse_num, class_="co_VerseNum").text)
                passuk = tr.find('span', class_="co_VerseText").text
                word_count += len(passuk.split())
                rashi = ''
                i += 1
                while i<len(trs):
                    tr = trs[i]
                    if 'Co_Rashi' not in tr.get('class'):
                        # hebrew table rows are NOT being displayes, so NOT progressed
                        break
                    # because of hebrew letter in Rashi, unified characters are needed
                    rashi_title = u''.join(tr.find('span', class_="co_RashiTitle").text).encode('utf-8')
                    word_count += len(rashi_title.split())
                    rashi_text = u''.join(tr.find('span', class_="co_RashiText").text).encode('utf-8')
                    word_count += len(rashi_text.split())
                    rashi += template('templates/rashi', rashi_text=rashi_text, rashi_title=rashi_title)
                    i += 1
                content += template('templates/psukim', passuk_num=passuk_num, passuk=passuk, rashi=rashi)
        return [content, word_count]

    def _get_page(self, topic, date_):
        url = 'https://www.chabad.org/' + \
                'dailystudy/' + topic + '.asp?' + \
                'tdate=' + self._convert_date(date_)
        self.browser.open(url)
        return self.browser.get_current_page()

    # in order to eayier store dates in DB and use them as links, without
    # path recognition problems
    def _convert_date(self, date_):
       return date_.replace('-', '/')

    # navigate between the different days of your daily learning
    def _days_prev_today_next(self, date_):
        dt = datetime.strptime(date_, '%m-%d-%Y')
        previous = dt - timedelta(1)
        previous = previous.strftime("%m-%d-%Y")
        today = datetime.today().strftime("%m-%d-%Y")
        next_ = dt + timedelta(1)
        next_ = next_.strftime("%m-%d-%Y")

        return [previous, today, next_]

    def _get_tanach_aid_by_book(self, book, chapter=None):
        aid = 0
        for key, val in tanach.items():
            if book == key:
                aid = val
                break
        url = 'https://www.chabad.org/library/bible.aspx?aid='+str(aid)
        new_url = self.browser.open(url)
        aid = new_url.url.split('/').pop()
        if chapter:
            aid = aid+chapter
        nach_url = 'https://www.chabad.org/library/bible_cdo/aid/'+str(aid)
        self.browser.open(nach_url)
        return self.browser.get_current_page() 
