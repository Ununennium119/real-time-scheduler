from task import Task
from scheduler import Scheduler

def main():
    tasks = [
        Task(id=1, arrival_time=0, execution_time=3, deadline=9),
        Task(id=2, arrival_time=1, execution_time=2, deadline=6),
        Task(id=3, arrival_time=2, execution_time=1, deadline=5),
        Task(id=4, arrival_time=3, execution_time=2, deadline=7),
        Task(id=5, arrival_time=0, execution_time=1, deadline=4),
    ]
    scheduler = Scheduler(tasks=tasks)

    bretly_schedule = scheduler.schedule_bretly(print_tree=True)
    print(f'Schedule using Bretly: {bretly_schedule}')
    scheduler.print_schedule(bretly_schedule)
    print(f'Maximum Lateness: {Scheduler.calculate_maximum_lateness(schedule=bretly_schedule)}')
    
    print('--------------------------------------------------')
    
    edf_schedule = scheduler.schedule_edf()
    print(f'Schedule using Bretly: {edf_schedule}')
    scheduler.print_schedule(bretly_schedule)
    print(f'Maximum Lateness: {Scheduler.calculate_maximum_lateness(schedule=edf_schedule)}')

if __name__ == '__main__':
    main()
