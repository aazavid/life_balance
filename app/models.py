from enum import Enum
from datetime import date, time
import uuid


class Direction:
    def __init__(self, name, color=None, description=None, goals=None, id=uuid.uuid4()):
        self.name = name
        self.color=color
        self.description = description
        self.goals = goals
        self.id = id


class GoalsType(Enum):
    GLOBAL = 1
    STRATEGY = 2
    YEARS = 3
    QUART = 4


class Goals:
    def __init__(self, name, type: GoalsType, description=None, direction_name=None, release_date=None, projects=None,
                 tasks=None, id=uuid.uuid4()):
        self.name = name
        self.type = type
        self.description = description
        self.direction_name = direction_name
        self.release_date = release_date
        self.projects = projects
        self.tasks = tasks
        self.id = id


class Project:
    def __init__(self, name, description=None, direction_name=None, release_date=None, tasks=None, id=uuid.uuid4()):
        self.name = name
        self.description = description
        self.direction_name = direction_name
        self.release_date = release_date
        self.tasks = tasks
        self.id = id


class Priority(Enum):
    HIGH = 1
    MEDIUM = 2
    LOW = 3


class Task:
    def __init__(self, name, description=None, date=None, time=None, repeat=None, repeat_time=None,
                 priority=Priority.MEDIUM, isDone=False, id=uuid.uuid4()):
        self.name = name
        self.description = description
        self.date = date
        self.time = time
        self.repeat = repeat
        self.repeat_time = repeat_time
        self.priority = priority
        self.isDone = isDone
        self.id = id


class Habit:
    def __init__(self, name, direction_name, description=None, id=uuid.uuid4()):
        self.name = name
        self.direction = direction_name
        self.description = description
        self.id = id
        self.history = []


class DataModels:
    def __init__(self):
        pass

    @staticmethod
    def get_tasks(tasks_date=date.today()):
        tasks = [Task("???????????? ???????????? ??", date=tasks_date, time=time(16, 25)),
                 Task("???????????? ???????????? B", date=tasks_date, time=time(6, 25)),
                 Task("???????????? ???????????? C", date=tasks_date, time=time(8, 0)),
                 Task("???????????? ???????????? D", date=tasks_date, time=time(12, 25)),
                 Task("???????????? ???????????? E", date=tasks_date, time=time(16, 20))
                 ]
        return tasks

    @staticmethod
    def get_directions():
        directions = [Direction("health"), Direction("finance"), Direction("relationship"), Direction("family"),
                      Direction("self-development"), Direction("routine"), Direction("rest"), Direction("business")]
        return directions

    @staticmethod
    def get_habits():
        habits = [Habit("walking", "health"), Habit("drink water", "health"), Habit("small talk", "relationship")]
        return habits

