import pytest
from space_weather_service.email import Mailer
from space_weather_service.controller import Controller
from os import path
from pubsub import pub
import smtplib


@pytest.fixture
def test_mailer():
    m = Mailer()
    return m


@pytest.fixture
def test_controller():
    c = Controller()
    return c


@pytest.fixture
def test_smtp():
    return smtplib.SMTP("localhost")


# Upon receiving new_config message
# Controller should separate info
# Controller should update email address in Mailer
def test_email_config(test_mailer, test_controller):
    # cInfo = ["x@y.com", "http://httpbin.org/post"]
    test_controller.MailView = test_mailer
    # pub.sendMessage("new_config", info=cInfo)
    test_controller.updateConfig(["x@y.com", "http://httpbin.org/post"])
    assert(test_mailer.addr == "x@y.com")


# Upon receiving make_email message
# Mailer should call new_plot to create a new history plot
def test_new_plot(test_mailer):
    test_mailer.formatMessage(0, 0, [1, 2, 3, 4])
    # assert that file exists
    assert(path.isfile('currentplot.png'))


# Mailer should generate a message of the proper type
# (Warning, Alert, Critical, Info)
def test_message_type(test_mailer):
    subjectStr = test_mailer.newSubject(10)
    assert("ALERT" in subjectStr)


def test_localhost(test_smtp):
    response, msg = test_smtp.ehlo()
    assert(response == 250)


# After email is generated
# Mailer should send email using SMTP
# def test_send_mail(test_smtp):
    # assert(False)
