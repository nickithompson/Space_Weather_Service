from pubsub import pub
from space_weather_service.model import Model
# from space_weather_service.api import Caller
# from space_weather_service.email import Mailer

from threading import Timer
import requests


class Controller:

    def __init__(self):
        self.model = Model()
        self.tracker = Tracker()
        # self.CallView = Caller()
        # self.MailView = Mailer()
        pub.subscribe(self.notifyViews, "new_levels")
        pub.subscribe(self.updateConfig, "new_config")

    # update: after tracker loops
    # get data and update model
    # def update(self):
    #    value = 1
    #    level = self.tracker.level
    #    self.model.newLevels(value, level)

    # notify: after model is updated
    # get data and history from model
    # send email and API call where applicable
    def notifyViews(self):
        # pfu exceeds 100, 10, 1,
        # or remains below 1 for 90 minutes

        history = self.model.History.copy()

        if(self.model.Level < 1):
            if(self.model.checkMins()):
                pub.sendMessage("make_email", level=self.model.Level,
                                value=self.model.Value, history=history)
                pub.sendMessage("make_request", level=self.model.Level,
                                value=self.model.Value)
                self.model.Count = 0
        elif(self.model.Level < 10):
            pub.sendMessage("make_email", level=self.model.Level,
                            value=self.model.Value, history=history)
        else:
            pub.sendMessage("make_email", level=self.model.Level,
                            value=self.model.Value, history=history)
            pub.sendMessage("make_request", level=self.model.Level,
                            value=self.model.Value)

    def updateConfig(self, info):
        email, endpoint = info
#        self.CallView.endURL = endpoint
#        self.MailView.addr = email

class Tracker:

    def __init__(self):
        self.level = 0
        self.loop()

    def loop(self):
        self.level += 1
        data = requests.get(
            'http://services.swpc.noaa.gov/text/goes-particle-flux-primary.txt')
        pub.sendMessage("data_update", data=data.text)
        self.timer = Timer(300, self.loop)
        self.timer.start()
