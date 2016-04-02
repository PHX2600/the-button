import tornado.ioloop
import tornado.web
import time
import os
import tornado.websocket
import json

counter = 0
kingOfTheHill = ""
scoreboard = dict()

app_dir = os.path.dirname(os.path.realpath(__file__))

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        global counter
        self.render(app_dir + "/public/index.html", scoreboard=scoreboard)

class ButtonHandler(tornado.web.RequestHandler):
    def post(self):
        global kingOfTheHill
        team = self.get_argument('team', None)
        kingOfTheHill = team
        if(scoreboard.get(kingOfTheHill) == None):
            scoreboard[kingOfTheHill] = 0

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

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/button", ButtonHandler),
        (r"/scoresocket", ScoreSocketHandler),
        (r"/css/(.*)", tornado.web.StaticFileHandler, {"path": app_dir + "/public/css/"}),
        (r"/js/(.*)", tornado.web.StaticFileHandler, {"path": app_dir + "/public/js/"}),
        (r"/images/(.*)", tornado.web.StaticFileHandler, {"path": app_dir + "/public/images/"}),
    ])

def checkButton():
    tornado.ioloop.IOLoop.current().add_timeout(time.time() + 1, checkButton)
    global counter
    global kingOfTheHill
    counter = counter+1
    if(kingOfTheHill != ""):
        old = scoreboard[kingOfTheHill]
        scoreboard[kingOfTheHill] = old+1
        ScoreSocketHandler.send_updates(json.dumps(scoreboard))

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().add_timeout(time.time() + 1, checkButton)
    tornado.ioloop.IOLoop.current().start()
