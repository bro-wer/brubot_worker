from .task import Task
from src.restConnector import RestConnector

class TaskManager(object):
    """docstring for TaskManager."""

    def __init__(self, configJsonPath):
        self.tasksList = []
        self.restConnector = RestConnector(configJsonPath)

    def findFreeTasks(self):
        print("TaskManager: findFreeTasks")
        self.tasksList = []
        tasksDicts = self.restConnector.getWaitingOrStartedTasks()

        for taskDict in tasksDicts.values():
            newTask = Task(configDict = taskDict)
            newTask.storeInLocal()
            self.tasksList.append(newTask)

    def processTasks(self):
        for task in self.tasksList:
            task.printme()
            self.__processTask(task)

    def __processTask(self, task):
        if task.isWaiting():
            self.__startTask(task)
        elif task.isStarted():
            self.__updateTaskStatus(task)

    def __startTask(self, task):
        print("TaskManager: __startTask")
        if self.restConnector.claimTask(task.id) == True:
            task.startJob()

    def __updateTaskStatus(self, task):
        print("TaskManager: __updateTaskStatus")
        self.restConnector.updateTaskStatus(id=task.id,
                                            status = task.getJobStatus())
