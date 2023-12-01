# import
import time
import webbrowser
import os
from tkinter import messagebox

# import project files
from commands import help, change_name, dir, edit_colors, cat, mkdir, rmdir, info_system, text_editor, ping, zatizeni
from app import app
from etc import colors, system
import __main__


def command_handler():

    while True:
        command = input(__main__.barva_1 + __main__.username + __main__.barva_2 + "@" + __main__.barva_3 + "local" + colors.reset + "$ ")
        command = command.replace(" ", "")
        command = command.lower()

        if command == "help":
            help.cmd()

        elif command == "app":
            app.cmd()

        elif command == "cmd":
            print("")
            system.welcome()

        elif command == "colorsreset":
            __main__.barva_1 = colors.lightblue
            __main__.barva_2 = colors.purple
            __main__.barva_3 = colors.green
            print("Barvy resetovány")

        elif command == "credits":
            messagebox.showinfo("Credits", "Děkuji za stáhnutí PyConsole. Toto je můj menší project. "
                                           "Koukni na můj web https://nejsem.online")

        elif command == "changeusername":
            change_name.cmd()

        elif command == "dir":
            dir.cmd()

        elif command == "cat":
            cat.cmd()

        elif command == "mkdir":
            mkdir.cmd()

        elif command == "rmdir":
            rmdir.cmd()

        elif command == "ping":
            ping.cmd()

        elif command == "system":
            info_system.cmd()

        elif command == "print":
            cmd_tisk_content = input(__main__.barva_1 + __main__.username + __main__.barva_2 + "@" + __main__.barva_3 + "local" + colors.yellow + "[print]" + colors.reset + "$ ")
            print(cmd_tisk_content)

        elif command == "texteditor":
            text_editor.cmd()

        elif command == "exit":
            cmd_odejit_content = input(colors.red + "Odejít? " + colors.reset + "[y/n] ")

            if cmd_odejit_content == "y":
                print(30 * "\n")
                system.logo()
                time.sleep(2)
                exit()

        elif command == "version":
            messagebox.showinfo("Verze", "PyConsole " + system.verze)

        elif command == "clear":
            os.system('cls')
            system.welcome()

        elif command == "web":
            webbrowser.open('https://nejsem.online/')

        elif command == "zatizeni":
            zatizeni.cmd()

        elif command == "editcolors":
            edit_colors.cmd()

        else:
            print(colors.red + "Invalid command\n")
