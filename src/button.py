import tornado.ioloop
import tornado.web
import time
import os
import tornado.websocket
import json
import sqlite3
import bcrypt

counter = 0
kingOfTheHill = ""
goingNegative = False
scoreboard = dict()
app_dir = os.path.dirname(os.path.realpath(__file__))
db = sqlite3.connect('database.db')

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
    def send_updates(cls, message):
        for buttoneer in cls.buttoneers:
            buttoneer.write_message(message)

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

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/button", ButtonHandler),
        (r"/scoresocket", ScoreSocketHandler),
        (r"/login", LoginHandler),
        (r"/css/(.*)", tornado.web.StaticFileHandler, {"path": app_dir + "/public/css/"}),
        (r"/js/(.*)", tornado.web.StaticFileHandler, {"path": app_dir + "/public/js/"}),
        (r"/images/(.*)", tornado.web.StaticFileHandler, {"path": app_dir + "/public/images/"}),
    ], cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
    login_url = "/")

def checkButton():
    tornado.ioloop.IOLoop.current().add_timeout(time.time() + 1, checkButton)
    global counter
    global kingOfTheHill
    global goingNegative
    counter = counter+1
    if(kingOfTheHill != ""):
        old = scoreboard[kingOfTheHill]
        if(goingNegative):
            scoreboard[kingOfTheHill] = old-1.5
            if(scoreboard[kingOfTheHill] < 0):
                scoreboard[kingOfTheHill] = 0
        else:
            scoreboard[kingOfTheHill] = old+1
        ScoreSocketHandler.send_updates(json.dumps(scoreboard))

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().add_timeout(time.time() + 1, checkButton)
    tornado.ioloop.IOLoop.current().start()
