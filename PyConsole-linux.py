# PyConsole
# Version 1.7 linux
# ©2023 by KralicekGamer


# import
import time
import string
import random
import os
import webbrowser
import platform
import socket

from datetime import datetime

# barvy
# formáty
reset = "\033[0m"
bold = "\033[01m"
disable = "\033[02m"
underline = "\033[04m"
reverse = "\033[07m"
strikethrough = "\033[09m"
invisible = "\033[08m"

# text
black = "\033[30m"
red = "\033[31m"
green = "\033[32m"
orange = "\033[33m"
blue = "\033[34m"
purple = "\033[35m"
cyan = "\033[36m"
lightgrey = "\033[37m"
darkgrey = "\033[90m"
lightred = "\033[91m"
lightgreen = "\033[92m"
yellow = "\033[93m"
lightblue = "\033[94m"
pink = "\033[95m"
lightcyan = "\033[96m"

# pozadí
bg_black = "\033[40m"
bg_red = "\033[41m"
bg_green = "\033[42m"
bg_orange = "\033[43m"
bg_blue = "\033[44m"
bg_purple = "\033[45m"
bg_cyan = "\033[46m"
bg_lightgrey = "\033[47m"


# welcome message
def welcome():
    print("PyConsole " + verze + "\n©2023 by KralicekGamer\n")


# verze
verze = "version 1.7 linux"


# logo
def logo():
    print(green + """
██████╗ ██╗   ██╗ █████╗  █████╗ ███╗  ██╗ ██████╗ █████╗ ██╗     ███████╗
██╔══██╗╚██╗ ██╔╝██╔══██╗██╔══██╗████╗ ██║██╔════╝██╔══██╗██║     ██╔════╝
██████╔╝ ╚████╔╝ ██║  ╚═╝██║  ██║██╔██╗██║╚█████╗ ██║  ██║██║     █████╗  
██╔═══╝   ╚██╔╝  ██║  ██╗██║  ██║██║╚████║ ╚═══██╗██║  ██║██║     ██╔══╝  
██║        ██║   ╚█████╔╝╚█████╔╝██║ ╚███║██████╔╝╚█████╔╝███████╗███████╗
╚═╝        ╚═╝    ╚════╝  ╚════╝ ╚═╝  ╚══╝╚═════╝  ╚════╝ ╚══════╝╚══════╝
""")


# core
def core():
    command = input(lightblue + username + purple + "@" + green + "local" + reset + "$ ")

    if command == "pomoc":
        print("""
APP-spustí danou aplikaci
    KALKULACKA-kalkulačka
    MADLIB-madlib hra
    HESLO-generace hesel
    KÁMEN-NŮŽKY-PAPÍR-kámen nůžky papír hra
ČAS-ukáže datum a čas
CREDITS-credity
DIR-vypíše soubory v aktuální složce
HODINY-otevře online hodiny
KOČKA-vytiskne soubor do console
MKDIR-vytvoří složku 
PING-pošle odezvu
RMDIR-smaže složku
SYSTEM-vypíše informace o systému
TISK-vytiskne input
ODEJIT-odejde
POMOC-pošle příkazy
VERZE-verze 
WEB-otevře můj web
ZATIZENI-zatizi aplikaci a pošle odezvu 
            """)
        core()

    elif command == "app":

        application = input("\033[94m" + username + "\033[35m" + "@" + green + "local" + "" + "\033[33m" + "[app]" + reset + "$ ")
        if application == "pomoc":
            print("""
    KALKULACKA-kalkulačka
        MADLIB-madlib hra
    HESLO-generace hesel
    KÁMEN-NŮŽKY-PAPÍR-kámen nůžky papír hra
                                  """)

        elif application == "kalkulacka":
            def add(a, b):
                return a + b

            def subtract(a, b):
                return a - b

            def multiply(a, b):
                return a * b

            def divide(a, b):
                if b != 0:
                    return a / b
                else:
                    return "Chyba: Nelze dělit nulou."

            operation = input("Zadejte operaci (+, -, *, /): ")
            num1 = float(input("Zadejte první číslo: "))
            num2 = float(input("Zadejte druhé číslo: "))

            if operation == "+":
                print(add(num1, num2))
            elif operation == "-":
                print(subtract(num1, num2))
            elif operation == "*":
                print(multiply(num1, num2))
            elif operation == "/":
                print(divide(num1, num2))
            else:
                print("Chybná operace.")

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
                print(red + "Error\n")
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
            core()

        else:
            print(red + "Invalid command\n")
            core()

    elif command == "čas":
        cmd_cas_cas = datetime.now()

        print(cmd_cas_cas.strftime("%d/%m/%Y %H:%M:%S"))
        core()

    elif command == "credits":
        print("Děkuji za stáhnutí PyConsole. Toto je můj menší project. Koukni na můj web https://nejsem.online")
        core()

    elif command == "dir":
        dir_files = os.listdir('.')
        for dir_file in dir_files:
            print(dir_file)
        print("")
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
            print(red + "Error\n")
            core()

    elif command == "mkdir":
        mk_dir_directory_name = input("Název složky: ")
        os.mkdir(mk_dir_directory_name)
        print("")
        core()

    elif command == "rmdir":
        rm_dir_directory_name = input("Název složky: ")
        os.rmdir(rm_dir_directory_name)
        print("")
        core()

    elif command == "ping":
        ping_start_time = time.time()
        print("pong")
        ping_end_time = time.time()
        ping_response_time = ping_end_time - ping_start_time
        if ping_response_time == 0:
            print("Odezva je: " + green + str(ping_response_time))

        elif ping_response_time > 1:
            print("Odezva je: " + red + str(ping_response_time))

        elif ping_response_time > 0:
            print("Odezva je: " + "\033[93m" + str(ping_response_time))

        else:
            print(red + "Error")

        print("")
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
        cmd_tisk_content = input("\033[94m" + username + "\033[35m" + "@" + green + "local" + "" + "\033[33m" + "[tisk]" + reset + "$ ")
        print(cmd_tisk_content)
        core()

    elif command == "odejit":
        cmd_odejit_content = input("\033[91mOdejít? " + "\033[0m[y/n] ")

        if cmd_odejit_content == "y":
            print(30 * "\n")
            logo()
            time.sleep(2)
            exit()

        else:
            core()

    elif command == "verze":
        print("PyConsole " + verze)
        core()

    elif command == "web":
        webbrowser.open('https://nejsem.online/')
        core()

    elif command == "zatizeni":
        zatizeni_start_time = time.time()
        print(999999 * "000000000" + reset)
        zatizeni_end_time = time.time()
        os.system('cls')
        welcome()
        zatizeni_response_time = zatizeni_end_time - zatizeni_start_time
        if zatizeni_response_time < 1:
            print("Odezva je: " + green + str(zatizeni_response_time))

        elif zatizeni_response_time < 2:
            print("Odezva je: " + red + str(zatizeni_response_time))

        elif zatizeni_response_time < 3:
            print("Odezva je: " + "\033[93m" + str(zatizeni_response_time))

        else:
            print(red + "Error")

        print("")
        core()

    else:
        print(red + "Invalid command\n")
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
