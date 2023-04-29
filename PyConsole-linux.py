# PyConsole
# Version 1.5.1 linux
# ©2023 by KralicekGamer


import string
import random
import time
import os
import webbrowser
import platform
import socket
from datetime import datetime


# colors
def prRed(skk):
    print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk):
    print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk):
    print("\033[93m {}\033[00m" .format(skk))
def prLightPurple(skk):
    print("\033[94m {}\033[00m" .format(skk))
def prPurple(skk):
    print("\033[95m {}\033[00m" .format(skk))
def prCyan(skk):
    print("\033[96m {}\033[00m" .format(skk))
def prLightGray(skk):
    print("\033[97m {}\033[00m" .format(skk))
def prBlack(skk):
    print("\033[98m {}\033[00m" .format(skk))


# welcome message
def welcome():
    print("\nPyConsole " + verze + "\n©2023 by KralicekGamer\n")


# verze
verze = "version 1.5.1 linux"


# logo
def logo():
    prGreen("""
██████╗ ██╗   ██╗ █████╗  █████╗ ███╗  ██╗ ██████╗ █████╗ ██╗     ███████╗
██╔══██╗╚██╗ ██╔╝██╔══██╗██╔══██╗████╗ ██║██╔════╝██╔══██╗██║     ██╔════╝
██████╔╝ ╚████╔╝ ██║  ╚═╝██║  ██║██╔██╗██║╚█████╗ ██║  ██║██║     █████╗  
██╔═══╝   ╚██╔╝  ██║  ██╗██║  ██║██║╚████║ ╚═══██╗██║  ██║██║     ██╔══╝  
██║        ██║   ╚█████╔╝╚█████╔╝██║ ╚███║██████╔╝╚█████╔╝███████╗███████╗
╚═╝        ╚═╝    ╚════╝  ╚════╝ ╚═╝  ╚══╝╚═════╝  ╚════╝ ╚══════╝╚══════╝
""")


# core(commands)
def core():
    command = input(username + "@local$ ")

    if command == "pomoc":
        print("""
APP-spustí danou aplikaci
ČAS-ukáže datum a čas
CMD/VERZE-startne nový terminál
CREDITS-credity
HODINY-otevře online hodiny
KOČKA-vytiskne soubor do console
SYSTEM-vypíše informace o systému
TISK-vytiskne input
TEA-tea mode
ODEJIT-odejde
POMOC-pošle příkazy
WEB-otevře můj web
            """)
        core()

    elif command == "app":

        application = input(username + "@local-[app]$ ")
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
                prRed("Error")
                core()

        elif application == "madlib":
            secret_world = input("Create secret world: ")

            def madlib():
                guess = input("Enter guess: ")

                if guess == secret_world:
                    print("You win")
                    core()

                else:
                    madlib()

            madlib()

        elif application == "heslo":
            try:
                length = int(input("Délka hesla: "))

                print('''\nZde vyber, co chceš mít v hesle za znaky
      1. Čísla
      2. Písmena
      3. Specialání znaky
      4. Vygenerovat heslo''')

                character_list = ""

                while True:
                    choice = int(input("Vyber číslo: "))
                    if choice == 1:

                        character_list += string.ascii_letters
                    elif choice == 2:

                        character_list += string.digits
                    elif choice == 3:

                        character_list += string.punctuation
                    elif choice == 4:
                        break
                    else:
                        print("Prosím zadej správný znak")

                password = []

                for i in range(length):
                    randomchar = random.choice(character_list)

                    password.append(randomchar)

                print("Tvoje heslo je " + "".join(password))
                core()

            finally:
                prRed("Error")
                core()

        elif application == "kámen-nůžky-papír":
            def kamen_nuzky_papir():

                choices = ["kámen", "nůžky", "papír"]
                odejit = ["odejit"]

                computer_choice = random.choice(choices)

                player_choice = input("Kámen, nůžky, nebo papír: ").lower()

                while player_choice not in choices:
                    player_choice = input("Kámen, nůžky, nebo papír: ").lower()

                if odejit == "odejit":
                    core()

                if player_choice == computer_choice:
                    print("Remíza!")
                elif player_choice == "kámen":
                    if computer_choice == "nůžky":
                        print("Vyhrál jsi!")
                    else:
                        print("Prohrál jsi.")
                elif player_choice == "nůžky":
                    if computer_choice == "papír":
                        print("Vyhrál jsi!")
                    else:
                        print("Prohrál jsi.")
                elif player_choice == "papír":
                    if computer_choice == "kámen":
                        print("Vyhrál jsi!")
                    else:
                        print("Prohrál jsi.")

                print("Bot si vybral: " + computer_choice)
                knp_1()

            def knp_1():
                knp = input("Hrát znovu? [y/n] ")
                if knp == "y":
                    kamen_nuzky_papir()

                else:
                    core()

            kamen_nuzky_papir()

        elif application == "pomoc":
            print("""
      KALKULACKA-kalkulačka
      MADLIB-madlib hra
      HESLO-generace hesel
      KÁMEN-NŮŽKY-PAPÍR-kámen nůžky papír hra
                              """)
            core()

        else:
            prRed("Invalid command")
            core()

    elif command == "čas":
        now = datetime.now()

        print(now.strftime("%d/%m/%Y %H:%M:%S"))
        core()

    elif command == "cmd":
        print("")
        welcome()
        core()

    elif command == "credits":
        logo()
        print("\n")
        print("""
PyConsole byla vytvořena uživatelem KralicekGamer
Tato console je součástí Project13
Děkuju za podporu 
""")
        core()

    elif command == "hodiny":
        webbrowser.open_new_tab('clock.html')
        print("Otevírám hodiny\n")
        core()

    elif command == "kočka":
        try:
            nazev = input("Zadej název souboru: ")
            soubor = open(nazev, "r")
            file = soubor.read()
            print(file)
            print("\n")
            soubor.close()
            core()

        finally:
            prRed("Error")
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
        tisk = input(username + "@local-[tisk]$ ")
        print(tisk)
        core()

    elif command == "tea":
        tea_spusit = input("Opravdu spusit režim tea? [y/n] ")
        if tea_spusit == "y":

            #core
            def jadro():
                kommand = input(username + "@lokal$ ")

                if kommand == "vitysknout":
                    tisk = input(username + "@lokal-[tysk]$ ")
                    print(tisk)
                    jadro()

                elif kommand == "odejyt":
                    odejit = input("Odejýt? [y/n] ")
                    print("\n")
                    logo()
                    time.sleep(2)

                    if odejit == "y":
                        exit()

                    else:
                        jadro()

                elif kommand == "vimazat":
                    os.system('cls')
                    welcome()
                    jadro()

                elif kommand == "segs":
                    print("A co sys jako mislel že se stane")
                    jadro()

                elif kommand == "hodyni":
                    webbrowser.open_new_tab('clock.html')
                    print("Otevírám ghodini\n")
                    jadro()

                elif kommand == "sistema":
                    print("\nYnformace o sistému\n")
                    print("Sistém: " + platform.system())
                    print("Relís: " + platform.release())
                    print("Platform veršn: " + platform.version())
                    print("Mašín veršm: " + platform.machine())
                    print("Název PíCí: " + socket.gethostname())
                    print("Ajpí adresa: " + socket.gethostbyname(socket.gethostname()))
                    print("Procesor: " + platform.processor() + "\n")
                    jadro()

                elif kommand == "časi":
                    now = datetime.now()

                    print(now.strftime("%d/%m/%Y %H:%M:%S"))
                    jadro()

                else:
                    prRed("Ynvalyd kommand")
                    jadro()
            jadro()

        else:
            core()

    elif command == "odejit":
        odejit = input("Odejít? [y/n] ")

        if odejit == "y":
            logo()
            time.sleep(2)
            exit()

        else:
            core()

    elif command == "verze":
        welcome()
        core()

    elif command == "web":
        webbrowser.open('https://kralicekgamer.ddns.net/')
        core()

    else:
        prRed("Invalid command")
        core()


# run
welcome()
username = input("Username: ")
core()
