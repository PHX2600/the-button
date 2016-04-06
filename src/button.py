import tornado.ioloop
import tornado.web
import time
import os
import tornado.websocket
import json
import sqlite3
import bcrypt
import operator
import random

kingOfTheHill = ""
goingNegative = False
scoreboard = dict()
app_dir = os.path.dirname(os.path.realpath(__file__))
db = sqlite3.connect('database.db')
#TODO Change this to 3600 for production
time_in_round = 20
flag_index = 0

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        user_id = self.get_secure_cookie("userid", max_age_days=1)
        if not user_id:
            return None
        return user_id

class MainHandler(BaseHandler):
    def get(self):
        self.render(app_dir + "/public/index.html")

class ButtonHandler(BaseHandler):
    @tornado.web.authenticated
    def post(self):
        global kingOfTheHill
        global goingNegative
        team = self.get_argument('team', None)
        if(team == kingOfTheHill):
            #They pressed the button twice in a row!
            goingNegative = True
        else:
            goingNegative = False
        kingOfTheHill = team
        if(scoreboard.get(kingOfTheHill) == None):
            scoreboard[kingOfTheHill] = 0

    @tornado.web.authenticated
    def get(self):
        teamname = self.get_current_user()
        self.render(app_dir + "/public/button.html", scoreboard=scoreboard, teamname=teamname)

class ScoreSocketHandler(tornado.websocket.WebSocketHandler):
    buttoneers = set()

    def open(self):
        ScoreSocketHandler.buttoneers.add(self)

    def on_close(self):
        ScoreSocketHandler.buttoneers.remove(self)

    @classmethod
    def send_updates(self, message):
        for buttoneer in self.buttoneers:
            buttoneer.write_message(message)

    @classmethod
    def send_flag_to(self, winner):
        global db
        cursor = db.cursor()
        cursor.execute("SELECT * from flags")
        rows = cursor.fetchall()
        flag_text = rows[flag_index]

        for buttoneer in self.buttoneers:
            if buttoneer.get_secure_cookie("userid") == winner:
                buttoneer.write_message('{"flag" : "' + str(flag_text[1]) + '"}')

class LoginHandler(BaseHandler):
    def post(self):
        team = self.get_argument('team', None)
        password = self.get_argument('password', None)
        if not team or not password:
            raise tornado.web.HTTPError(403)

        global db
        cursor = db.cursor()
        packaged = (team, ) #no idea why you have to do this
        cursor.execute("SELECT * from teams WHERE name=? LIMIT 1", packaged)
        row = cursor.fetchone()
        if not row:
            raise tornado.web.HTTPError(403)

        teamname = row[1]
        score = row[2]
        passhash = row[3]

        password = password.encode('utf-8')
        if passhash == bcrypt.hashpw(password, passhash.encode('utf-8')) and teamname == team:
            self.set_secure_cookie("userid", teamname, httponly=True, expires_days=1)
        else:
            raise tornado.web.HTTPError(403)

class CaptchaHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        captcha = ""
        images = dict()
        #Six digit random number
        for i in range(6):
            num = random.randint(0, 9)
            captcha = captcha + str(num)
            filename = ""
            if(num == 0):
                filename = "30e81ddd887ee347f68f9434ad3b8b0c.png"
            elif(num == 1):
                filename = "a90a90b322ea5a99d19f589fa42fb32c.png"
            elif(num == 2):
                filename = "20b6f4d2cb789ae32a8b267924bae39a.png"
            elif(num == 3):
                filename = "0df2eba54857d80164b2644b53d62529.png"
            elif(num == 4):
                filename = "6f5cd4a2329bd9ab39f3c2f8a0635e76.png"
            elif(num == 5):
                filename = "14ccbf3db9c27aa41e9449e245172faf.png"
            elif(num == 6):
                filename = "3f278f90f33c4238b676a165186047b7.png"
            elif(num == 7):
                filename = "9e928437e18355adc3136c42613a1bb2.png"
            elif(num == 8):
                filename = "ab32f699fe869f591007fe5095fb59ab.png"
            elif(num == 9):
                filename = "d342c63cb19f14fb8024df589756a73c.png"

            images[i] = filename

        self.write(json.dumps(images))

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/button", ButtonHandler),
        (r"/scoresocket", ScoreSocketHandler),
        (r"/login", LoginHandler),
        (r"/captcha", CaptchaHandler),
        (r"/css/(.*)", tornado.web.StaticFileHandler, {"path": app_dir + "/public/css/"}),
        (r"/js/(.*)", tornado.web.StaticFileHandler, {"path": app_dir + "/public/js/"}),
        (r"/images/(.*)", tornado.web.StaticFileHandler, {"path": app_dir + "/public/images/"}),
    ], cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
    login_url = "/")

def checkButton():
    tornado.ioloop.IOLoop.current().add_timeout(time.time() + 1, checkButton)
    global kingOfTheHill
    global goingNegative
    if(kingOfTheHill != ""):
        old = scoreboard[kingOfTheHill]
        if(goingNegative):
            scoreboard[kingOfTheHill] = old-1.5
            if(scoreboard[kingOfTheHill] < 0):
                scoreboard[kingOfTheHill] = 0
        else:
            scoreboard[kingOfTheHill] = old+1
        ScoreSocketHandler.send_updates(json.dumps(scoreboard))

def resetRound():
    tornado.ioloop.IOLoop.current().add_timeout(time.time() + time_in_round, resetRound)
    global kingOfTheHill
    global scoreboard
    global flag_index
    winner = max(scoreboard.iteritems(), key=operator.itemgetter(1))[0]
    #Delete the scoreboard to start again
    scoreboard = dict()
    kingOfTheHill = ""
    ScoreSocketHandler.send_flag_to(winner)
    flag_index = flag_index + 1

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().add_timeout(time.time() + 1, checkButton)
    tornado.ioloop.IOLoop.current().add_timeout(time.time() + time_in_round, resetRound)
    tornado.ioloop.IOLoop.current().start()
