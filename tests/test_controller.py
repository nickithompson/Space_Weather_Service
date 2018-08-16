import pytest
from threading import Timer
from pubsub import pub
from space_weather_service.controller import Controller, Tracker
# from space_weather_service.Model.model import Model

@pytest.fixture
def test_controller():
    C = Controller()
    return C


# Upon receiving a data update message,
# controller should get new data
#def test_update(test_controller):
#    startVal = test_controller.model.Value
#    pub.sendMessage("data_update")
#    assert(test_controller.model.Value != startVal)


@pytest.fixture
def test_tracker():
    T = Tracker()
    return T


# tracker should cycle every 5 minutes
def test_timer(test_tracker):
    L1 = test_tracker.level

    def check():
        testTimer.cancel()
        L2 = test_tracker.level
        assert(L1 != L2)

    testTimer = Timer(300, check)
    testTimer.start()


# when tracker cycles,
# tracker should send data_update message
# controller should get data and update model
def test_updated_level(test_tracker, test_controller):

    def compareLevels():
        testTimer.cancel()
        # L1 = test_controller.level
        trackerLevel = test_tracker.level
        modelLevel = test_controller.model.level
        assert(trackerLevel == modelLevel)

    testTimer = Timer(300, compareLevels)
    testTimer.start()
