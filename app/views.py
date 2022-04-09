from tkinter import *
from controlers import Controller


class Views:

    def show_today_frame(self, frame, tasks, habits):
        index_row = 1
        self.clear_frame(frame)
        title = Label(frame, text="Today")
        title.grid(row=0, column=0, sticky=N)
        tasks.sort(key=lambda x: x.time)
        for task in tasks:
            task_label_time = Label(frame, text=task.time.strftime("%H:%M"), padx=0)
            task_label_time.grid(row=index_row, column=0)

            task_label_name = Label(frame, text=task.name)
            task_label_name.grid(row=index_row, column=1)

            task_check_box_is_done = Checkbutton(frame)
            task_check_box_is_done.grid(row=index_row, column=2)
            if task.isDone:
                task_check_box_is_done.select()

            index_row = index_row + 1

        habit_title = Label(frame, text="Habits")
        index_row += 10
        habit_title.grid(row=index_row, column=1)

        for habit in habits:
            index_row = index_row + 1
            label_name_habit = Label(frame, text=habit.name)
            label_name_habit.grid(row=index_row, column=0)

            habit_check_box_is_done = Checkbutton(frame)
            habit_check_box_is_done.grid(row=index_row, column=1)

    def show_month_frame(self, frame):
        self.clear_frame(frame)
        title = Label(frame, text="Month")
        title.grid(row=0, column=0, sticky=N)

    def show_week_frame(self, frame):
        self.clear_frame(frame)
        title = Label(frame, text="Week")
        title.grid(row=0, column=0, sticky=N)

    def clear_frame(self, frame):
        for widgets in frame.winfo_children():
            widgets.destroy()
