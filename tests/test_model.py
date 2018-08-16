import pytest
from space_weather_service.model import Model


@pytest.fixture
def test_model():
    M = Model()
    return M


# Upon receiving data_update message,
# Model should read last line of data text
# Model should parse P > 10 value
# Model should calculate level
def test_lines(test_model):
    testFile = open("tests/goes-particle-flux-primary.txt")
    test_data = testFile.read()
    testFile.close()
    test_model.parseData(test_data)
    test_value = 1.58 * 10**(-1)
    assert(test_model.Value == test_value)


# If level is below 1,
# Controller calls Model to check history
# Model should return true if level has been below 1 for 90 minutes
# Model should return false if not
def test_history(test_model):
    test_model.Count = 20
    assert(test_model.checkMins())
