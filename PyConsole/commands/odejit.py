import time
import __main__
from etc import etc


def cmd():
    cmd_odejit_content = input("\033[91mOdejít? " + "\033[0m[y/n] ")

    if cmd_odejit_content == "y":
        print(30 * "\n")
        etc.logo()
        time.sleep(2)
        exit()

    else:
        __main__.core()
