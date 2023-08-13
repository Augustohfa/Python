import os
import json

# Json library

filePath = '/Users/augustoazevedo/Documents/Code/Python_Git/ExerciciosModulo3/'
filePath += 'ToDoList.json'


# Mudar o que eu salvo e uso no 'only_tasks' para um arquivo JSon, fazer
# Read and write nele
# Functions


def save(task):
    with open(filePath, 'a') as json_file:
        json.dump(
            task, json_file, ensure_ascii=False
        )


def load():
    data = []
    with open(filePath, 'r', encoding='utf8') as json_file:
        data = json.load(json_file)
    print(data)
    return data


only_tasks = [[], []]


try:
    jsonFile = open(filePath, 'x')
except FileExistsError:
    imported_tasks = (load())
    for i in imported_tasks:
        only_tasks[0].append(i)


def add_task(task):
    if not task:
        return
    else:
        global items_count
        items_count = len(only_tasks[0]) + 1
        only_tasks[0].append(task)
        json_tasks.append(task)
        # Append to JSON here
        list_tasks(only_tasks)
        save(json_tasks)


def task_done(tasks,  done_task):
    task_index = tasks[0].index(done_task)

    if done_task in tasks[0]:
        # Removing from undone lists
        tasks[0].pop(task_index)  # change it to read()

        # Adding to done lists
        tasks[1].append(done_task)  # Remove task from JSON

    else:
        print(
            'The task you are trying to do is already done '
            'or were not added at all!'
        )
    list_tasks(tasks)


def undo_task(tasks, undone_task):
    task_index = tasks[1].index(undone_task)
    global items_count
    items_count += 1

    if undone_task in tasks[1]:
        # Removing from undone lists
        tasks[1].pop(task_index)

        # Adding to done lists
        tasks[0].append(undone_task)
    else:
        print(
            'The task you are trying to do is already undone '
            'or were not added at all!'
        )
    list_tasks(tasks)


def list_tasks(tasks):
    if not tasks:
        print('No tasks remaning!')

    else:
        times_passed = 0
        print(separator)
        print('Undone taks: ')
        # For inside for to iterate over nested lists
        for inner_lists in tasks:
            count = 0
            times_passed += 1
            if times_passed == 2:
                print(separator)
                print('Done Tasks: ')
            for items in inner_lists:
                count += 1
                print(f'Task Nº {count} ->  {items}', sep='\n')

        print(separator)


# Declaration
separator = '-' * 30
json_tasks = []
# Main Loop

while True:

    print(
        'Type one of the following commands: '
        'done, undone, list or clear '
        'or the task you wish to add'
    )
    user_input = input('Type the task or the commands: ')

    commands = {
        'done': lambda: task_done(only_tasks, 'teste'),
        'list': lambda: list_tasks(only_tasks),
        'undone': lambda: undo_task(only_tasks, 'teste'),
        'clear': lambda: os.system('clear'),
        'add': lambda: add_task(user_input)
    }

    command_func = commands.get(user_input) if commands.get(user_input) \
        is not None else commands['add']

    command_func()

jsonFile.close()
