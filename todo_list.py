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
    print('5. List Tasks')
    print('6. Quit')


def get_option():
    try:
        option = int(input('\nSelect an option... '))
        print(f'Option {option} selected...')
    except ValueError:
        option = 0
        print('This is not number, please, digit integer numbers from 1 to 6...')
    return option


def get_index():
    try:
        index = int(input('Select the number of task:'))
    except ValueError:
        index = 0
        print('This is not number, please, digit integer numbers from 1 to 6...')
    return index


def isValidOption(option):
    if option < 1 or option > 6:
        return False
    return True


def create_task():
    name = input('Name: ')
    due_date = input('Date: ')
    return Task(name, due_date)


def add_task(toDo):
    print('Creating Task...\n')
    task = create_task()
    toDo.append(task)
    print('\n---Task Created---')


def edit_task(toDo):
    print('Editing Task...\n')
    index = get_index()
    toDo[index-1] = create_task()
    print('\n---Task Edited---')


def done_task(toDo):
    print('Marking Task...\n')
    index = get_index()
    value = input('Press 1 if it is done, if not press any button...')
    if value == '1':
        done = True
    else:
        done = False
    toDo[index-1].done = done
    print('\n---Task Marked Done---')


def delete_task(toDo):
    print('Deleting Task...\n')
    index = get_index()
    del toDo[index-1]
    print('\n---Task Deleted---')


def title_list():
    print('\n****************************')
    print(' ****** TASKS LIST ******')
    print('****************************')


def list_tasks(toDo):
    index = 0
    for task in toDo:
        index += 1
        task.print_data(index)


def process(option, toDo):
    message = '\nFunc is not implemented yet.\nSorry for inconvenience.'
    if option == 1:
        add_task(toDo)
    elif option == 2:
        edit_task(toDo)
    elif option == 3:
        done_task(toDo)
    elif option == 4:
        delete_task(toDo)
    elif option == 5:
        title_list()
        list_tasks(toDo)


def execute():
    option = None
    todo_list = []

    while option != 6:
        menu()
        option = get_option()
        if not isValidOption(option):
            print('\nOption not valid, try from 1 to 6.')
            continue
        process(option, todo_list)


execute()
