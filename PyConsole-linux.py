# PyConsole
# Version 1.6 linux
# ©2023 by KralicekGamer


# import
import string
import random
import time
import os
import webbrowser
import platform
import socket

from datetime import datetime


# barvy
"""
formáty
    reset = \033[0m
    bold = \033[01m
    disable = \033[02m
    underline = \033[04m
    reverse = \033[07m
    strikethrough = \033[09m
    invisible = \033[08m

text
    black = \033[30m
    red = \033[31m
    green = \033[32m
    orange = \033[33m
    blue = \033[34m
    purple = \033[35m
    cyan = \033[36m
    lightgrey = \033[37m
    darkgrey = \033[90m
    lightred = \033[91m
    lightgreen = \033[92m
    yellow = \033[93m
    lightblue = \033[94m
    pink = \033[95m
    lightcyan = \033[96m

pozadí
    black = \033[40m
    red = \033[41m
    green = \033[42m
    orange = \033[43m
    blue = \033[44m
    purple = \033[45m
    cyan = \033[46m
    lightgrey = \033[47m
"""


# welcome message
def welcome():
    print("PyConsole " + verze + "\n©2023 by KralicekGamer\n")


# verze
verze = "version 1.6 linux"


# logo
def logo():
    print("\033[32m" + """
██████╗ ██╗   ██╗ █████╗  █████╗ ███╗  ██╗ ██████╗ █████╗ ██╗     ███████╗
██╔══██╗╚██╗ ██╔╝██╔══██╗██╔══██╗████╗ ██║██╔════╝██╔══██╗██║     ██╔════╝
██████╔╝ ╚████╔╝ ██║  ╚═╝██║  ██║██╔██╗██║╚█████╗ ██║  ██║██║     █████╗  
██╔═══╝   ╚██╔╝  ██║  ██╗██║  ██║██║╚████║ ╚═══██╗██║  ██║██║     ██╔══╝  
██║        ██║   ╚█████╔╝╚█████╔╝██║ ╚███║██████╔╝╚█████╔╝███████╗███████╗
╚═╝        ╚═╝    ╚════╝  ╚════╝ ╚═╝  ╚══╝╚═════╝  ╚════╝ ╚══════╝╚══════╝
""")


# core
def core():
    command = input("\033[94m" + username + "\033[35m" + "@" + "\033[32m" + "local" + "\033[0m" + "$ ")

    if command == "pomoc":
        print("""
APP-spustí danou aplikaci
    KALKULACKA-kalkulačka
    MADLIB-madlib hra
    HESLO-generace hesel
    KÁMEN-NŮŽKY-PAPÍR-kámen nůžky papír hra
ČAS-ukáže datum a čas
CMD-startne nový terminál
CREDITS-credity
HODINY-otevře online hodiny
KOČKA-vytiskne soubor do console
SYSTEM-vypíše informace o systému
TISK-vytiskne input
ODEJIT-odejde
POMOC-pošle příkazy
VERZE-ukáže verzi terminálu
WEB-otevře můj web
            """)
        core()

    elif command == "app":

        application = input("\033[94m" + username + "\033[35m" + "@" + "\033[32m" + "local" + "" + "\033[33m" + "[app]" + "\033[0m" + "$ ")
        if application == "kalkulacka":
            try:
                number_1 = int(input('První číslo: '))
                number_2 = int(input('Druhé číslo: '))

                print('{} + {} = '.format(number_1, number_2))
                print(number_1 + number_2)
                print("")

                print('{} - {} = '.format(number_1, number_2))
                print(number_1 - number_2)
                print("")

                print('{} * {} = '.format(number_1, number_2))
                print(number_1 * number_2)
                print("")

                print('{} / {} = '.format(number_1, number_2))
                print(number_1 / number_2)
                print("")

                core()

            finally:
                print("\033[31m" + "Error\n")
                core()

        elif application == "madlib":
            secret_world = input("Create secret world: ")

            def app_madlib():
                app_madlib_guess = input("Enter guess: ")

                if app_madlib_guess == secret_world:
                    print("You win")
                    core()

                else:
                    app_madlib()

            app_madlib()

        elif application == "heslo":
            try:
                length = int(input("Délka hesla: "))

                print('''\nZde vyber, co chceš mít v hesle za znaky
    1. Čísla
    2. Písmena
    3. Specialání znaky
    4. Vygenerovat heslo''')

                app_password_character_list = ""

                while True:
                    choice = int(input("Vyber číslo: "))
                    if choice == 1:

                        app_password_character_list += string.ascii_letters
                    elif choice == 2:

                        app_password_character_list += string.digits
                    elif choice == 3:

                        app_password_character_list += string.punctuation
                    elif choice == 4:
                        break
                    else:
                        print("Prosím zadej správný znak")

                app_password_password = []

                for i in range(length):
                    randomchar = random.choice(app_password_character_list)

                    app_password_password.append(randomchar)

                print("Tvoje heslo je " + "".join(app_password_password))
                core()

            finally:
                print("\033[31m" + "Error\n")
                core()

        elif application == "kámen-nůžky-papír":
            def app_knp():

                app_knp_choices = ["kámen", "nůžky", "papír"]

                app_knp_computer_choice = random.choice(app_knp_choices)

                app_knp_player_choice = input("Kámen, nůžky, nebo papír: ").lower()

                while app_knp_player_choice not in app_knp_choices:
                    app_knp_player_choice = input("Kámen, nůžky, nebo papír: ").lower()

                if app_knp_player_choice == app_knp_computer_choice:
                    print("Remíza!")
                elif app_knp_player_choice == "kámen":
                    if app_knp_computer_choice == "nůžky":
                        print("Vyhrál jsi!")
                    else:
                        print("Prohrál jsi.")
                elif app_knp_player_choice == "nůžky":
                    if app_knp_computer_choice == "papír":
                        print("Vyhrál jsi!")
                    else:
                        print("Prohrál jsi.")
                elif app_knp_player_choice == "papír":
                    if app_knp_computer_choice == "kámen":
                        print("Vyhrál jsi!")
                    else:
                        print("Prohrál jsi.")

                print("Bot si vybral: " + app_knp_computer_choice)
                app_knp_pa()

            def app_knp_pa():
                app_knp_pa_vyber = input("Hrát znovu? [y/n] ")
                if app_knp_pa_vyber == "y":
                    app_knp()

                else:
                    core()

            app_knp()

        elif application == "pomoc":
            print("""
      KALKULACKA-kalkulačka
      MADLIB-madlib hra
      HESLO-generace hesel
      KÁMEN-NŮŽKY-PAPÍR-kámen nůžky papír hra
                              """)
            core()

        else:
            print("\033[31m" + "Invalid command\n")
            core()

    elif command == "čas":
        cmd_cas_cas = datetime.now()

        print(cmd_cas_cas.strftime("%d/%m/%Y %H:%M:%S"))
        core()

    elif command == "cmd":
        print("")
        welcome()
        core()

    elif command == "credits":
        print("Děkuji za stáhnutí PyConsole. Toto je můj menší project Koukni na můj web https://kralicekgamer.ddns.net/")
        core()

    elif command == "hodiny":
        webbrowser.open_new_tab('clock.html')
        print("Otevírám hodiny\n")
        core()

    elif command == "kočka":
        try:
            cmd_kocka_filename = input("Zadej název souboru: ")
            cmd_kocka_file = open(cmd_kocka_filename, "r")
            cmd_kocka_file_content = cmd_kocka_file.read()
            print(cmd_kocka_file_content)
            print("\n")
            cmd_kocka_file.close()
            core()

        finally:
            print("\033[31m" + "Error\n")
            core()

    elif command == "sex":
        print("A co sis jako myslel, že se stane")
        core()

    elif command == "system":
        print("\nInformace o systému\n")
        print("Systém: " + platform.system())
        print("Relese: " + platform.release())
        print("Platform version: " + platform.version())
        print("Machine version: " + platform.machine())
        print("Název PC: " + socket.gethostname())
        print("Ip adresa: " + socket.gethostbyname(socket.gethostname()))
        print("Procesor: " + platform.processor() + "\n")
        core()

    elif command == "tisk":
        cmd_tisk_content = input("\033[94m" + username + "\033[35m" + "@" + "\033[32m" + "local" + "" + "\033[33m" + "[tisk]" + "\033[0m" + "$ ")
        print(cmd_tisk_content)
        core()

    elif command == "odejit":
        cmd_odejit_content = input("\033[91mOdejít? " + "\033[0m[y/n] ")

        if cmd_odejit_content == "y":
            print(30*"\n")
            logo()
            time.sleep(2)
            exit()

        else:
            core()

    elif command == "verze":
        print("PyConsole " + verze)
        core()

    elif command == "web":
        webbrowser.open('https://kralicekgamer.ddns.net/')
        core()

    else:
        print("\033[31m" + "Invalid command\n")
        core()


# run
welcome()
run_username_file = "username.txt"
if os.path.exists(run_username_file):
    with open(run_username_file, "r") as file:
        username = file.read().strip()
else:
    username = input("Username: ")
    with open(run_username_file, "w") as file:
        file.write(username)

core()
