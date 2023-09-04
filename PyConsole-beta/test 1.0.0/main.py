# PyConsole - linux
# Version 2.1
# ©2023 by KralicekGamer

# import
import os


# project files
from commands.etc import colors, system
from commands import pomoc, odejit, app, cmd, credits, change_name, dir, kočka, mkdir, rmdir, info_system, ping, tisk, verze

if __name__ == "__main__":
    system.welcome()
    run_username_file = "commands/etc/username.txt"
    if os.path.exists(run_username_file):
        with open(run_username_file, "r") as file:
            username = file.read().strip()
    else:
        username = input("Username: ")
        with open(run_username_file, "w") as file:
            file.write(username)

while True:
    command = input(colors.lightblue + username + colors.purple + "@" + colors.green + "testing" + colors.reset + "$ ")
    command = command.replace(" ", "")
    command = command.lower()

    if command == "pomoc":
        pomoc.cmd()

    elif command == "app":
        app.cmd()

    elif command == "cmd":
        cmd.cmd()

    elif command == "credits":
        credits.cmd()

    elif command == "changeusername":
        change_name.cmd()

    elif command == "dir":
        dir.cmd()

    elif command == "kočka":
        kočka.cmd()

    elif command == "mkdir":
        mkdir.cmd()

    elif command == "rmdir":
        rmdir.cmd()

    elif command == "ping":
        ping.cmd()

    elif command == "system":
        info_system.cmd()

    elif command == "tisk":
        tisk.cmd()

    elif command == "odejit":
        odejit.cmd()

    elif command == "verze":
        verze.cmd()

    else:
        print(colors.red + "Invalid command\n")
