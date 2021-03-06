# MyDaily:
Personal Learning Compendium, enjoy it.
This is the first release. Version 0.1. Here you can see a demo: [MyDaily](http://mydaily.online-shiurim.org)
This application, is a simple parser from [chabad.org](https://chabad.org) which can be also extended to work with other websites as well. It is designed for the use with a smartphone.
By now there are four books in the english version available: 
 - HaYom Yom
 - Tora with Rashi
 - Rambam One Chapter a Day
 - Tanach with Rashi, starting with Sefer Yehoshua
If you want me any books to add, let me know! The project was developed, within couple of days, to get it running and progress in learning. So few things need to be done (much) better. I hope to get to upgrade it soon. Check the ToDo list below, and your welcome to suggest some Features. 

By now (ver 0.1.) the user still needs to navigate himself, to let the app know, that he wants the next section of a specific book, otherwise he will get the same book as to the date he registered.

Concerning the bottle and the uwsgi framework, I am not sure, if I will stay with them, because originally when I started, I was looking for something small and local, but by now, I think it has more potential than that, let's see where it goes.

## How to install
Using Python3. This app runs on the lightweight bottlepy framework, using mechanicalsoup for parsing.
```
git clone git@github.com:bor1e/mydaily.git
pip install -r requirements
```
## Start Server
```python
 python3 setup.py
```
The application is now running on your localhost, on `port=8770`

## Add User with specific username
The `username` is only needed to keep a record where the user holding. 
After starting the server just call the following url and add the desired username  `localhost:8770/adduser/<username>`.
Now you are redirected to the specific entry of the user. Eventually a login, or other tactics can be implemented to secure that point for anyone else.
`username` needs to be be only alpha-characters!

## Add books and other sources
If you want me to add any books, please let me know!
I am currently testing and working on better, more dynamical book structures and proper interfaces to be easy exchangeable und fluently interacting. Learning about other sources will enable me to define the interfaces for adding books better.
Planning to add following books, in weekly basis:
- Halacha
- Mishna
- Sefer Mizwot

## ToDo:
Next steps are:
- create Object-Oriented approach for books, like an interface including all needed methods, trying to analyse html tree structure, defining reoccuring tags etc.
- some unittesting would be nice, to avoid typos
- adding a FAQ, descibing how to have same settings on phone, tablet and pc, including a contact possibility for personalification options.
- error handling, especially of db
- now every request is being sent to chabad.org, and there are no text being saved in DB, which leads to overload. I think I will include also the current copy of all the sections, replacing specific section.
- eventually adjust the reading time to real learning speed
- defining order of books

## Bugs:
Due to a fast developement, and some shortcuts, including testing, this app has bugs. Let's find and fix them =).

Please report bugs!

## Support:
You like that project? Let me know by supporting me via [Paypal](paypal.me/OnlineShiurim)
