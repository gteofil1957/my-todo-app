FILEPATH = "todos.txt"

def get_todos(filepath = FILEPATH):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath = FILEPATH):
    """ It's a function by Teo
        It gets a list of todos and has a default argument 'filepath'
        """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

