PATH = "todos.txt"


def get_todos(path=PATH):
    """ Read a text file and return the list of to-do items"""
    with open(path, "r") as file:
        todos_list = file.readlines()
    return todos_list


def set_todos(todos_list, path=PATH):
    """ Write the to-do items list in a text file"""
    with open(path, "w") as file:
        file.writelines(todos_list)


if __name__ == "__main__":
    print("Hello from functions")
