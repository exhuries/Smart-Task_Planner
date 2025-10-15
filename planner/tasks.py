from datetime import datetime, timedelta

class Task:
    def __init__(self, name, duration=1, deadline=None, subtasks=None):
        self.name = name
        self.duration = duration  # in hours
        self.subtasks = subtasks if subtasks else []
        self.deadline = deadline  # datetime object

    def is_primitive(self):
        return len(self.subtasks) == 0

    def __repr__(self):
        return f"Task(name={self.name}, duration={self.duration}, deadline={self.deadline})"

