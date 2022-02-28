# Menu Actions
add = 1
edit = 2
done = 3
delete = 4
listTask = 5
close = 6
minimumOption = 1
maximumOption = 6


class Task:

    def __init__(self, name, due_date):
        self.name = name
        self.due_date = due_date
        self.done = False

    def print_data(self, index):
        print('{0}. Task: {1}, Date: {2}, Done: {3}.'.format(index, self.name, self.due_date, self.done))


def menu():
    print('\n****************************')
    print('*** to DO list by Daniel ***')
    print('****************************')
    print('\nSelect an Option: ')
    print('1. Add Task')
    print('2. Edit Task')
    print('3. Mark Done')
    print('4. Delete Task')
    print('5. View Tasks')
    print('6. Quit')


def title_list():
    print('\n****************************')
    print(' ****** TASKS LIST ******')
    print('****************************')


def get_option():
    try:
        option = int(input('\nSelect an option... '))
        print(f'Option {option} selected...')
    except ValueError:
        option = 0
        print('This is not number, please, digit integer numbers from 1 till 6...')
    return option


def create_task():
    name = input('Name: ')
    due_date = input('Date: ')
    return Task(name, due_date)


def isValidOption(option):
    if option < 1 or option > 6:
        return False
    return True


def new_list():
    return []


def add_task(task, toDo):
    toDo.append(task)


def process_add_task(toDo):
    print('Creating Task...\n')
    task = create_task()
    add_task(task, toDo)
    print('\n---Task Created---')


def all_tasks(toDo):
    index = 0
    for task in toDo:
        index += 1
        task.print_data(index)


def get_index():
    try:
        index = int(input('Select the number of task:'))
    except ValueError:
        index = 0
        print('This is not number, please, digit integer numbers from 1 till 6...')
    return index


def edit_task(index, new_task, toDo):
    toDo[index-1] = new_task


def setIsDone():
    value = input('Press 1 if it is done, if not press any button...')
    if value == '1':
        return True
    return False


def doneTask(index, done, toDo):
    toDo[index-1].done = done


def processDoneTask(toDo):
    print('Marking Task...\n')
    index = get_index()
    done = setIsDone()
    doneTask(index, done, toDo)
    print('\n---Task Marked---')


def process_edit_task(toDo):
    print('Editing Task...\n')
    index = get_index()
    task = create_task()
    edit_task(index, task, toDo)
    print('\n---Task Edited---')


def deleteTask(index, toDo):
    del toDo[index-1]


def processDeleteTask(toDo):
    print('Deleting Task...\n')
    index = get_index()
    deleteTask(index, toDo)
    print('\n---Task Deleted---')


def process(option, toDo):
    print('The process is started...')
    message = '\nFunc is not implemented yet.\nSorry for inconvenience.'
    if option == 1:
        process_add_task(toDo)
    elif option == 2:
        process_edit_task(toDo)
    elif option == 3:
        processDoneTask(toDo)
    elif option == 4:
        processDeleteTask(toDo)
    elif option == 5:
        title_list()
        all_tasks(toDo)


def execute():
    option = None
    toDo = new_list()

    while option != 6:
        menu()
        option = get_option()
        if not isValidOption(option):
            print('\nOption not valid, try from 1 till 6.')
            continue
        process(option, toDo)


execute()
# task = functions.create_task()
# task.print_data(5)
