# PyConsole
# Version pre-relese 2.0 windows
# ©2023 by KralicekGamer

# project files
from etc import etc
from commands import pomoc, odejit, app, cmd, credits, dir, hodiny, kočka, mkdir, rmdir, system, text_editor, ping, tisk, verze, vymazat, web, zatizeni

# import
import os


def core():
    command = input(etc.lightblue + username + etc.purple + "@" + etc.green + "local" + etc.reset + "$ ")

    if command == "pomoc":
        pomoc.cmd()

    elif command == "app":
        app.cmd()

    elif command == "cmd":
        cmd.cmd()

    elif command == "credits":
        credits.cmd()

    elif command == "dir":
        dir.cmd()

    elif command == "hodiny":
        hodiny.cmd()

    elif command == "kočka":
        kočka.cmd()

    elif command == "mkdir":
        mkdir.cmd()

    elif command == "rmdir":
        rmdir.cmd()

    elif command == "ping":
        ping.cmd()

    elif command == "system":
        system.cmd()

    elif command == "tisk":
        tisk.cmd()

    elif command == "text editor":
        text_editor.cmd()

    elif command == "odejit":
        odejit.cmd()

    elif command == "verze":
        verze.cmd()

    elif command == "vymazat":
        vymazat.cmd()

    elif command == "web":
        web.cmd()

    elif command == "zatizeni":
        zatizeni.cmd()

    else:
        print(etc.red + "Invalid command\n")
        core()
    core()


run_username_file = "etc/username.txt"
if os.path.exists(run_username_file):
    with open(run_username_file, "r") as file:
        username = file.read().strip()
else:
    username = input("Username: ")
    with open(run_username_file, "w") as file:
        file.write(username)


if __name__ == "__main__":
    etc.welcome()
    core()
