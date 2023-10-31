
def get_todo(filepath="todos.txt"):  # also you can change this arg in following call function and assign new value.
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todo(todos_arg,filepath="todos.txt"):
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


if __name__ == "__main__": # "__main__" means execute this directly not import, if you import, it'll be "function".
    print("Hello")
