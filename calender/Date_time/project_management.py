from datetime import *

class Project:

    def __init__(self, name, startDate, endDate):
        self.name = name
        self.startDate = startDate
        self.endDate = endDate
        self.tasks = []

    def addTask(self, task):
        self.tasks.append(task)


class Task:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration
        self.resources = []

    def addResources(self, resource):
        self.resources.append(resource)


class Resource:
    def __init__(self, name, skill):
        self.name = name
        self.skill = skill


project = Project("AI", date(2020, 2, 8), date(2020, 12, 8))
task = Task("create bot", 99)
resource = Resource("Maaz", "python")
project.addTask(task)
task.addResources(resource)


for eachTask in project.tasks:
    print(eachTask.name)
    for eachResource in eachTask.resources:
        print(eachResource.name)
        print(eachResource.skill)