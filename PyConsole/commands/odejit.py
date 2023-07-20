import time
from commands.etc import system


def cmd():
    cmd_odejit_content = input("\033[91mOdejít? " + "\033[0m[y/n] ")

    if cmd_odejit_content == "y":
        print(30 * "\n")
        system.logo()
        time.sleep(2)
        exit()
