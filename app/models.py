from enum import Enum
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

