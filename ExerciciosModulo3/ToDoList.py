import os


# Functions

def add_task(task):
    if not task:
        return
    else:
        global items_count
        items_count = len(tasks_to_print[0]) + 1
        tasks_to_print[0].append(f'Task Nº {items_count} -> {task}')

        only_tasks[0].append(task)
    list_tasks(tasks_to_print)


def task_done(tasks, tasks_to_print, done_task):
    task_index = tasks[0].index(done_task)

    if done_task in tasks[0]:
        # Removing from undone lists
        tasks[0].pop(task_index)
        tasks_to_print[0].pop(task_index)

        # Adding to done lists
        tasks[1].append(done_task)
        tasks_to_print[1].append(done_task)

    else:
        print(
            'The task you are trying to do is already done '
            'or were not added at all!'
        )
    list_tasks(tasks_to_print)


def undo_task(tasks, tasks_to_print, undone_task):
    task_index = tasks[1].index(undone_task)
    global items_count
    items_count += 1

    if undone_task in tasks[1]:
        # Removing from undone lists
        tasks[1].pop(task_index)
        tasks_to_print[1].pop(task_index)

        # Adding to done lists
        tasks[0].append(undone_task)
        tasks_to_print[0].append(f'Task Nº {items_count} -> {undone_task}')

    else:
        print(
            'The task you are trying to do is already undone '
            'or were not added at all!'
        )
    list_tasks(tasks_to_print)


def list_tasks(tasks):
    if not tasks:
        print('No tasks remaning!')

    else:
        count = 0
        print(separator)
        print('Undone taks: ')
        # For inside for to iterate over nested lists
        for inner_lists in tasks:
            count += 1
            if count == 2:
                print(separator)
                print('Done Tasks: ')
            for items in inner_lists:
                print(items, sep='\n')

        print(separator)


# Declaration
tasks_to_print = [[], []]
only_tasks = [[], []]
separator = '-' * 30

# Main Loop
while True:
    print(
        'Type one of the following commands: '
        'done, undone, list or clear '
        'or the task you wish to add'
    )
    user_input = input('Type the task or the commands: ')

    commands = {
        'done': lambda: task_done(only_tasks, tasks_to_print, 'teste'),
        'list': lambda: list_tasks(tasks_to_print),
        'undone': lambda: undo_task(only_tasks, tasks_to_print, 'teste'),
        'clear': lambda: os.system('clear'),
        'add': lambda: add_task(user_input)
    }

    command_func = commands.get(user_input) if commands.get(user_input) \
        is not None else commands['add']
    command_func()
# while True:

#
#     if user_input == 'done':
#         task_done(only_tasks, tasks_to_print, 'teste')
#         list_tasks(tasks_to_print)
#         continue
#
#     elif user_input == 'list':
#         list_tasks(tasks_to_print)
#         continue
#
#     elif user_input == 'clear':
#         os.system('clear')
#         break
#
#     elif user_input == 'undone':
#         undo_task(only_tasks, tasks_to_print, 'teste')
#         list_tasks(tasks_to_print)
#         continue
#
#     else:
#         add_task(user_input)
#         list_tasks(tasks_to_print)
