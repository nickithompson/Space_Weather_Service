from email.mime.multipart import MIMEMultipart
from pubsub import pub
from os import path
from email.mime.image import MIMEImage
from matplotlib import pyplot
import smtplib
# import smtpd


class Mailer:

    def __init__(self):
        self.addr = None
        self.fromAddr = "service@localhost"
        pub.subscribe(self.newMessage, "make_email")

    def sendMessage(self, msg):
        s = smtplib.SMTP('localhost')
        s.sendmail(self.fromAddr, self.addr, msg.as_string())
        s.quit()

    def formatMessage(self, level, value, history):
        self.newPlot(history)
        msg = MIMEMultipart()
        msg['Subject'] = self.newSubject(level)
        msg['From'] = self.fromAddr
        msg.preamble = 'Value = %.2f' % value
        # attach plot to message
        if(path.isfile('currentplot.png')):
            fp = open('currentplot.png', 'rb')
            img = MIMEImage(fp.read())
            fp.close()
            msg.attach(img)
        return msg

    def newSubject(self, level):
        if(level < 1):
            return "INFO: >10MeV levels below 1pfu"
        elif(level < 10):
            return "WARNING: >10MeV levels above 1pfu"
        elif(level < 100):
            return "ALERT: >10MeV levels above 10pfu"
        else:
            return "CRITICAL: >10MeV levels above 100pfu"

    def newMessage(self, level, value, history):
        msg = self.formatMessage(level, value, history)
        self.sendMessage(msg)

    def newPlot(self, history):
        # construct plot
        # pyplot.ioff()
        fig = pyplot.figure()
        pyplot.plot(history)
        pyplot.ylabel('Particles at >10MeV')
        # export to file
        pyplot.savefig('currentplot.png')
        pyplot.close()
