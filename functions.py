import os

FILENAME = 'todos.txt'


def create_file(filename):
    with open(filename, 'w') as file:
        pass


def get_todos(filename=FILENAME):
    """
    Read files and returns a list of todos
    :param filename: The file containing the todos
    :return: The list of todos
    """
    if not os.path.exists(filename):
        create_file(filename)

    with open(filename, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos, filename=FILENAME):
    """
    Writes down the new todos into the file specified
    :param todos: New list of todos
    :param filename: The file containing the todos
    """
    with open(filename, 'w') as file:
        for todo_local in todos:
            if '\n' not in todo_local:
                todo_local = todo_local + '\n'
            file.write(todo_local.capitalize())


def show(todos):
    print('--- List of todos ---')
    for index, item in enumerate(todos):
        item = item.strip('\n')
        print(f'{index + 1}: {item.capitalize()}')
    if len(todos) != 0:
        print('--- ---')


def index_in_interval(index, todos):
    return not (0 < index <= len(todos))


if __name__ == "__main__":
    print('something')
