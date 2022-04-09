from tkinter import *
from models import *
from controlers import DataController


def make_today_frame(display):
    clear_frame(display)
    title = Label(display, text="Today")
    title.grid(row=0, column=0, sticky=N)

    # display tasks
    index_row = 1
    tasks = DataController.get_tasks()
    tasks.sort(key=lambda x: x.time)
    for task in tasks:
        task_label_time = Label(display, text=task.time.strftime("%H:%M"), padx=0)
        task_label_time.grid(row=index_row, column=0)

        task_label_name = Label(display, text=task.name)
        task_label_name.grid(row=index_row, column=1)

        task_check_box_is_done = Checkbutton(display)
        task_check_box_is_done.grid(row=index_row, column=2)
        if task.isDone:
            task_check_box_is_done.select()

        index_row = index_row + 1

    # display habits
    habit_title = Label(display, text="Habits")
    index_row += 10
    habit_title.grid(row=index_row, column=1)
    habits = DataController.get_habits()
    for habit in habits:
        index_row = index_row + 1
        label_name_habit = Label(display, text=habit.name)
        label_name_habit.grid(row=index_row, column=0)

        habit_check_box_is_done = Checkbutton(display)
        habit_check_box_is_done.grid(row=index_row, column=1)


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


def clear_frame(frame):
    for widgets in frame.winfo_children():
        widgets.destroy()


class App(Tk):
    def __init__(self):
        super().__init__()

        self.geometry("1200x800")
        self.title("Life Planer")
        self.iconbitmap("../img/schedule.ico")
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
