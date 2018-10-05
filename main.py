import os
from src.taskManager import TaskManager

if __name__ == '__main__':
    taskManager = TaskManager(os.path.join("settings", "config.json"))
    taskManager.findFreeTasks()
    taskManager.processTasks()
