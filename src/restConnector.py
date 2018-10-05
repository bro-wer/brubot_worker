import json
import http.client



class RestConnector(object):
    """docstring for RestConnector."""

    def __init__(self, configJsonPath):
        print("RestConnector: __init__")
        self.configDict = {}
        self.__extractJson(configJsonPath)

    def __extractJson(self, configJsonPath):
        with open(configJsonPath) as f:
            self.configDict = json.load(f)["restUrls"]

    def getAllTasks(self):
        print("RestConnector: getAllTasks")
        try:
            return self.getRestRepsonse(self.configDict["getAllTasks"])
        except Exception as e:
            return {}

    def getWaitingTasks(self):
        print("RestConnector: getWaitingTasks")
        try:
            return self.getRestRepsonse(self.configDict["getWaitingTasks"])
        except Exception as e:
            return {}

    def getWaitingOrStartedTasks(self):
        print("RestConnector: getWaitingTasks")
        try:
            return self.getRestRepsonse(self.configDict["getWaitingOrStartedTasks"])
        except Exception as e:
            return {}

    def claimTask(self, id):
        return False

    def updateTaskStatus(self, id, status):
        pass

    def getRestRepsonse(self, restUrl):
        conn = http.client.HTTPSConnection(self.configDict["mainUrl"])
        conn.request("GET", restUrl)
        response = conn.getresponse()
        decodeResponse = response.read().decode('ascii')
        dictResponse = json.loads(decodeResponse)

        #for elemkey, elemvalue in dictResponse.items():
        #    print("\n#{}".format(str(elemkey)))
        #    for key, value in elemvalue.items():
        #        print("\t{}: {}".format(key, value))

        return dictResponse
