import datetime, json
import http.client, urllib.parse

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
        params = urllib.parse.urlencode({'taskId': id})
        headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
        conn = http.client.HTTPSConnection(self.configDict["mainUrl"])
        conn.request("POST", self.configDict["claimTask"], params, headers)
        response = conn.getresponse()

        print("claimTask response.status = " + str(response.status))

        if response.status == "200":
            return True
        return False

    def updateTaskStatus(self, id, status):
        params = urllib.parse.urlencode({'taskId': id,
                                         'status': status,
                                         'timestamp': str(datetime.datetime.now())})
        headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
        conn = http.client.HTTPSConnection(self.configDict["mainUrl"])
        conn.request("POST", self.configDict["updateTaskStatus"], params, headers)
        response = conn.getresponse()


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
