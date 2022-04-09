from models import Task, Direction, Habit
from datetime import date, time


class DataController:
    def __init__(self):
        pass

    @staticmethod
    def get_tasks(tasks_date=date.today()):
        tasks = [Task("Решить задачу А", date=tasks_date, time=time(16, 25)),
                 Task("Решить задачу B", date=tasks_date, time=time(6, 25)),
                 Task("Решить задачу C", date=tasks_date, time=time(8, 0)),
                 Task("Решить задачу D", date=tasks_date, time=time(12, 25)),
                 Task("Решить задачу E", date=tasks_date, time=time(16, 20))
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
