# MyDailyLearning:
This is the first release. Version 0.1. Here you can see a demo: 
This application, is a simple parser from [chabad.org](https://chabad.org) which can be also extended to work with other websites as well. It is designed for the use with a smartphone.
By now there are four books in the englsih version available: 
 - HaYom Yom
 - Tora with Rashi
 - Rambam One Chapter a Day
 - Tanach with Rashi, starting with Sefer Yehoshua
If you want me any books to add, let me know! The project was developed, within couple of days, to get it running and progress in learning. So few things needs to be done better, check the ToDo list below, and your welcome to suggest some Features. 

By now (ver 0.1.) the user still needs to navigate himself, to let the app know, that he wants the next section of a specific book, otherwise he will get the same book as to the date he registered everyday.

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

## ToDo:
Next steps are:
- now every request is being sent to chabad.org, and there are no text being saved in DB, which leads to overload. I think I will include also the current copy of the section
- adding JS scrollspy, updating the db when user finished a portion, without any input from user, when specific user interested.
- eventually update the reading time 

## Bugs:
Due to a fast developement, and some shortcuts, including testing, this app has bugs. Let's find and fix them =).

Please report bugs!

## Support:
You like that project? Let me know by supporting me via [Paypal](paypal.me/OnlineShiurim)
