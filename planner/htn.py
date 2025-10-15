from datetime import datetime, timedelta

class HTNPlanner:
    def __init__(self):
        pass

    def create_plan(self, task, start_time=None):
        if start_time is None:
            start_time = datetime.now()
        plan = []
        self._plan_task(task, start_time, plan)
        return plan

    def _plan_task(self, task, current_time, plan):
        if task.is_primitive():
            end_time = current_time + timedelta(hours=task.duration)
            if task.deadline and end_time > task.deadline:
                print(f"⚠️ Task '{task.name}' exceeds deadline!")
            plan.append({
                "task": task.name,
                "start": current_time,
                "end": end_time
            })
            return end_time
        else:
            for subtask in task.subtasks:
                current_time = self._plan_task(subtask, current_time, plan)
            return current_time

