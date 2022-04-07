from tkinter import *
from enum import Enum
from datetime import date, time
import uuid


class Direction:
    def __init__(self, name, description=None, goals=None, id=uuid.uuid4()):
        self.name = name
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


def make_today_frame(display):
    clear_frame(display)
    title = Label(display, text="Today")
    title.grid(row=0, column=0, sticky=N)
    index_row = 1
    tasks = get_tasks()
    tasks.sort(key=lambda x: x.time)
    for task in tasks:
        label = Label(display, text=task.name)
        label.grid(row=index_row, column=0)
        index_row = index_row + 1


def make_month_frame(display):
    clear_frame(display)
    title = Label(display, text="Month")
    title.grid(row=0, column=0, sticky=N)


def make_week_frame(display):
    clear_frame(display)
    title = Label(display, text="Week")
    title.grid(row=0, column=0, sticky=N)


def cursor_position(event):
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))


def get_tasks(tasks_date=date.today()):
    tasks = [Task("Решить задачу А", date=tasks_date, time=time(16, 25)),
             Task("Решить задачу B", date=tasks_date, time=time(6, 25)),
             Task("Решить задачу C", date=tasks_date, time=time(8, 0)),
             Task("Решить задачу D", date=tasks_date, time=time(12, 25)),
             Task("Решить задачу E", date=tasks_date, time=time(16, 20))
             ]
    return tasks


def clear_frame(frame):
    for widgets in frame.winfo_children():
        widgets.destroy()


class App(Tk):
    def __init__(self):
        super().__init__()

        self.geometry("1200x800")
        self.title("Life Planer")
        # configure the grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=5)
        self.columnconfigure(3, weight=1)

        self.create_widgets()

    def create_widgets(self):
        panel_frame = Frame(self, name="panel")
        panel_frame.grid(row=0, column=0, sticky=NW)
        content_frame = Frame(self, name="content", width=200)
        content_frame.grid(row=0, column=1, sticky=N)
        button1 = Button(panel_frame, text="Today", width=10, command=lambda: make_today_frame(content_frame))
        button1.grid(row=0, column=0)
        button2 = Button(panel_frame, text="Week", width=10, command=lambda: make_week_frame(content_frame))
        button2.grid(row=1, column=0)
        button3 = Button(panel_frame, text="Month", width=10, command=lambda: make_month_frame(content_frame))
        button3.grid(row=2, column=0)
        principle_frame = Frame(self, name="principles", width=100)
        principle_frame.grid(row=0, column=2, sticky=NE)
        title_principle = Label(principle_frame, text="Принципы")
        title_principle.grid(row=0, column=0)
        make_today_frame(content_frame)


if __name__ == '__main__':
    # todo: add view for screen today
    app = App()
    app.mainloop()
