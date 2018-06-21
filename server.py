from bottle import default_app, route, run, static_file, template, install, request, response, redirect
import bottle
from bottle_sqlite import SQLitePlugin
from datetime import date, datetime
import random
from parser import Parser
from functools import wraps
import logging

app=application=default_app()

logger = logging.getLogger('logfile')

# set up the logger
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('logfile.log')
formatter = logging.Formatter('%(msg)s')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def log_to_logger(fn):
    '''
    Wrap a Bottle request so that a log line is emitted after it's handled.
    (This decorator can be extended to take the desired logger as a param.)
    '''
    @wraps(fn)
    def _log_to_logger(*args, **kwargs):
        request_time = datetime.now()
        actual_response = fn(*args, **kwargs)
        # modify this to log exactly what you need:
        logger.info('%s %s %s %s %s' % (request.remote_addr,
                                        request_time,
                                        request.method,
                                        request.url,
                                        response.status))
        return actual_response
    return _log_to_logger

install(SQLitePlugin(dbfile='./bookmarks.db'))
install(log_to_logger)

@route('/')
def init(db):
    # check if user_id is set
    if request.get_cookie("user_id"):
        user_id = request.get_cookie("user_id")
        return user(db=db, user=user_id)

    # TODO eventually a collision possible by two users -> better user recognition
    # eventually a timestamp combination could be helpful, but 
    # this is meant for 'visitors' for friends, a username should be provided
    user_id = random.randint(10000000,99999999)
    response.set_header('Set-Cookie', 'user_id='+str(user_id))
    response.add_header('Set-Cookie', 'expires='+str(24*24*60*60*1000)) # cookie expires after 24 days
    today = date.today().strftime("%m-%d-%Y")
    # speed for 136 words, I needed 42 secs. which is 136/42 words per second 
    # how much minutes do I need for 1000 words?
    # reading_speed = (1000 / (136/42))/60
    db.execute('insert into bookmark values (?,?,?,?,?,?)', (user_id, today, today, today, 15785, (136/42.0),))
    return user(db=db, user=str(user_id))

@route('/adduser/<username>')
def adduser(db, username):
    assert username.isalpha()
    today = date.today().strftime("%m-%d-%Y")
    if not request.get_cookie("user_id"):
        response.set_header('Set-Cookie', 'user_id='+str(username))
        response.add_header('Set-Cookie', 'expires='+str(24*24*60*60*1000)) # cookie expires after 24 days

    db.execute('insert into bookmark values (?,?,?,?,?,?)', (username, today, today, today, 15785, (136/42.0),))
    redirect('/')

@route('/setuser/<username>')
def setuser(username):
    assert username.isalpha()
    response.set_header('Set-Cookie', 'user_id='+str(username))
    redirect('/')

#@route('/:user')
def user(db, user):
    tora = db.execute('select tora from bookmark where user = ?', (user,)).fetchone()[0]
    hayomyom = db.execute('select hayomyom from bookmark where user = ?', (user,)).fetchone()[0]
    rambam = db.execute('select rambam from bookmark where user = ?', (user,)).fetchone()[0]
    tanach = db.execute('select tanach from bookmark where user = ?', (user,)).fetchone()[0]
    books = {
        'hayomyom': str(hayomyom),
        'tora': str(tora),
        'rambam': str(rambam),
        'tanach': tanach,
        }
    speed = db.execute('select reading_speed from bookmark where user = ?', (user,)).fetchone()[0]
    visitors = str(db.execute('select count(*) from bookmark').fetchone()[0])
    parser = Parser(user=user, books=books, speed=speed)
    return template('templates/index', content=parser.content(visitors))

@route('/new_source', method='POST')
def add_source(db):
    source = request.forms.get('new_source')
    #TODO: ERROR handling
    db.execute('insert into sources values (?)', (source,))
    redirect('/')

@route('/js/<filename>')
def js(filename):
    return static_file(filename, root='./js/')

@route('/webfonts/<filename>')
@route('/css/<filename>')
def css(filename):
    return static_file(filename, root='./css/')

@route('/<category>/<next>')
def next(db, category, next):
    assert category.isalpha()
    if not request.get_cookie("user_id"):
        redriect('/#'+category)
    user = request.get_cookie("user_id")
    # TODO check for success
    query = 'update bookmark set ' + category + ' = \'' + next +'\' where user = \'' + user +'\';' 
    db.execute(query)

    redirect('/#'+str(category))

class StripPathMiddleware(object):
    '''
    Get that slash out of the request
    '''
    def __init__(self, a):
        self.a = a
    def __call__(self, e, h):
        e['PATH_INFO'] = e['PATH_INFO'].rstrip('/')
        return self.a(e, h)

if __name__ == '__main__':
    run(app=StripPathMiddleware(app), host='0.0.0.0', port=8770, debug=True, quiet=True)
