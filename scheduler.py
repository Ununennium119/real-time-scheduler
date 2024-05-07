from typing import Optional
from task import Task

class Scheduler:
    def __init__(self, tasks: list[Task]) -> None:
        self.tasks: list[Task] = tasks

    def schedule_bretly(self, current_schedule: list[Task] = [], print_tree: bool = False) -> Optional[list[Task]]:
        # Check if the newly added task causes us to miss any deadline
        current_time = sum(task.execution_time for task in current_schedule)
        if len(current_schedule) > 0:
            for task in self.tasks:
                if (task not in current_schedule) or (task == current_schedule[-1]):
                    if current_time > task.deadline:
                        if print_tree:
                            print(' x')
                        return None
        if print_tree:
            print()
        
        # Return the schedule if current schedule has all tasks
        if len(current_schedule) == len(self.tasks):
            return current_schedule

        # Add new tasks to schedule
        for task in self.tasks:
            # Only add the new task if its not in the schedule and is already arrived
            if task not in current_schedule:
                if print_tree:
                    print('|' + '--' * (len(current_schedule) + 1) + f'{task.id}', end='')
                if task.arrival_time <= current_time:
                    current_schedule.append(task)
                    feasible_schedule = self.schedule_bretly(current_schedule, print_tree=print_tree)
                    if feasible_schedule:
                        return feasible_schedule
                    current_schedule.remove(task)
                elif print_tree:
                    print(' x')
    
    def schedule_edf(self) -> Optional[list[Task]]:
        current_time = 0
        current_schedule = []
        while len(current_schedule) < len(self.tasks):
            arrived_tasks = [task for task in self.tasks if (task.arrival_time <= current_time) and (task not in current_schedule)]
            task = min(arrived_tasks, key=lambda task: task.deadline)
            current_schedule.append(task)
            current_time += task.execution_time
        return current_schedule
    
    @classmethod
    def calculate_maximum_lateness(cls, schedule: list[Task]) -> int:
        current_time = 0
        max_lateness = float('-inf')
        for task in schedule:
            current_time += task.execution_time
            lateness = current_time - task.deadline
            if lateness > max_lateness:
                max_lateness = lateness
        return max_lateness
    
    @classmethod
    def print_schedule(cls, schedule: list[Task]):
        print('|', end='')
        for task in schedule:
            print(f'{task.id}|' * task.execution_time, end='')
        print()
