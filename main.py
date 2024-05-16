from task import Task
from scheduler import Scheduler
from anytree import Node, RenderTree

def main():
    tasks = [
        Task(id=1, arrival_time=0, execution_time=3, deadline=9),
        Task(id=2, arrival_time=1, execution_time=2, deadline=6),
        Task(id=3, arrival_time=2, execution_time=1, deadline=5),
        Task(id=4, arrival_time=3, execution_time=2, deadline=7),
        Task(id=5, arrival_time=0, execution_time=1, deadline=4),
    ]
    scheduler = Scheduler(tasks=tasks)

    print("Scheduling using Bretly algorithm...")
    root_node = Node('')
    bretly_schedule = scheduler.schedule_bretly(root_node)
    render_tree(root_node)
    print(f'Schedule: {bretly_schedule}')
    scheduler.print_schedule(bretly_schedule)
    print(f'Maximum Lateness: {Scheduler.calculate_maximum_lateness(schedule=bretly_schedule)}')
    
    print('--------------------------------------------------')
    
    print("Scheduling using non-preemptive EDF algorithm...")
    edf_schedule = scheduler.schedule_edf()
    print(f'Schedule: {edf_schedule}')
    scheduler.print_schedule(bretly_schedule)
    print(f'Maximum Lateness: {Scheduler.calculate_maximum_lateness(schedule=edf_schedule)}')

def render_tree(root_node: Node):
    for pre, _, node in RenderTree(root_node):
        print("%s%s" % (pre, node.name))

if __name__ == '__main__':
    main()
