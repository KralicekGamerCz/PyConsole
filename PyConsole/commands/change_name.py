import __main__


def cmd():
    username_file = "commands/etc/username.txt"
    new_username = input("Username: ")
    with open(username_file, "w") as file:
        file.truncate()
        file.write(new_username)
    with open(username_file, "r") as file:
        __main__.username = file.read().strip()
