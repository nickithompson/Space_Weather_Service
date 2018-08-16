from pubsub import pub
from collections import deque


class Model:

    def __init__(self):
        self.Value = 0
        self.Level = 0
        self.Count = 0
        self.History = deque(maxlen=90)
        pub.subscribe(self.parseData, "data_update")

    def newLevels(self, value, level):
        self.Value = value
        self.Level = level
        self.updateHistory()
        pub.sendMessage("new_levels")

    def parseData(self, data):
        lines = data.splitlines()
        mostRecent = lines[len(lines) - 1].split()
        valueStr, expStr = mostRecent[8].split("e")
        value = float(valueStr) * 10**(float(expStr))
        level = int(value)
        self.newLevels(value, level)

    # check if level has been < 1 for 90 mins
    def checkMins(self):
        mins = 5 * self.Count
        return (mins >= 90)

    def updateHistory(self):
        if(self.Level < 1):
            self.Count += 1
        else:
            self.Count = 0
        item = self.Value
        self.History.append(item)
