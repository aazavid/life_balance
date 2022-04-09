from tkinter import *
from views import Views
from controlers import Controller


class Application(Tk):
    def __init__(self):
        super().__init__()

        self.geometry("1200x800")
        self.title("Life Planer")
        self.iconbitmap("../img/schedule.ico")
        # configure the grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=5)
        self.columnconfigure(3, weight=1)
        self.views = Views()
        self.controller = Controller(self.views)

        self.create_widgets()

    def create_widgets(self):
        panel_frame = Frame(self, name="panel")
        panel_frame.grid(row=0, column=0, sticky=NW)
        content_frame = Frame(self, name="content", width=200)
        content_frame.grid(row=0, column=1, sticky=N)

        button1 = Button(panel_frame, text="Today", width=10,
                         command=lambda: self.controller.make_today_frame(content_frame))
        button1.grid(row=0, column=0)

        button2 = Button(panel_frame, text="Week", width=10,
                         command=lambda: self.controller.make_week_frame(content_frame))
        button2.grid(row=1, column=0)

        button3 = Button(panel_frame, text="Month", width=10,
                         command=lambda: self.controller.make_month_frame(content_frame))
        button3.grid(row=2, column=0)

        principle_frame = Frame(self, name="principles", width=100)
        principle_frame.grid(row=0, column=2, sticky=NE)
        title_principle = Label(principle_frame, text="Принципы")
        title_principle.grid(row=0, column=0)
        self.controller.make_today_frame(content_frame)