import json
import os

class Task(object):
    """docstring for Task."""

    def __init__(self, configDict):
        self.configDict = configDict
        self.localDir = os.path.join(os.getcwd(), "tasksData")
        self.__parseDictData()


    def __parseDictData(self):
        self.id = self.configDict["id"]
        self.taskName = self.configDict["taskName"]
        self.status = self.configDict["status"]
        self.type = self.configDict["type"]


    def storeInLocal(self):
        with open(os.path.join(self.localDir, str(self.id) + ".json" ), 'w') as outfile:
            json.dump(self.configDict, outfile)

    def readFromLocal(self, taskId):
        with open(os.path.join(self.localDir, taskId + ".json" )) as f:
            self.configDict = json.load(f)
            self.__parseDictData()

    def isWaiting(self):
        return self.status == "NS"

    def isStarted(self):
        return self.status == "ST"

    def startJob(self):
        print("Task: startJob")

    def getJobStatus(self):
        print("Task: getJobStatus")
        status = {"status" : "ST",
                  "message": "some test message"}
        return status

    def printme(self):
        print("\nTASK DETAILS")
        print("\tid: {}".format(str(self.id)))
        print("\ttaskName: {}".format(str(self.taskName)))
        print("\tstatus: {}".format(str(self.status)))
        print("\ttype: {}".format(str(self.type)))
