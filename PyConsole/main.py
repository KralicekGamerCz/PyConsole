# PyConsole		            
# Version 1.3.2             
# ©2024 by KralicekGamer

# import
import os

# import project files
from etc import system, colors
import command_handler

color_1 = colors.lightblue
color_2 = colors.purple
color_3 = colors.green

if __name__ == "__main__":
    system.welcome()
    run_username_current_directory = os.path.dirname(os.path.abspath(__file__))
    run_username_file = os.path.join(run_username_current_directory, "etc/username.txt")

    if os.path.exists(run_username_file):
        with open(run_username_file, "r") as file:
            username = file.read().strip()
    else:
        username = input("Username: ")
        with open(run_username_file, "w") as file:
            file.write(username)
    file.close()
    command_handler.command_handler()
