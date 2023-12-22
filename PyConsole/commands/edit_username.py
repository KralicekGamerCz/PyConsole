import __main__
import os
import sys


def cmd():
    cmd_username_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    username_file = os.path.join(cmd_username_dir, "etc/username.txt")
    new_username = input("Username: ")

    with open(username_file, "w") as file:
        file.truncate()
        file.write(new_username)
    with open(username_file, "r") as file:
        __main__.username = file.read().strip()
    file.close()
