from models import DataModels


class Controller:

    def __init__(self, view):
        self.view = view

    def make_today_frame(self, frame):
        tasks = DataModels.get_tasks()
        habits = DataModels.get_habits()
        self.view.show_today_frame(frame, tasks, habits)

    def make_month_frame(self, frame):
        self.view.show_month_frame(frame)

    def make_week_frame(self, frame):
        self.view.show_week_frame(frame)

    @staticmethod
    def cursor_position(event):
        x, y = event.x, event.y
        print('{}, {}'.format(x, y))


