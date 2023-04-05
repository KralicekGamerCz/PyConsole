# PyConsole
# Version 1.4
# ©2023 by KralicekGamer


import string
import random
import time
import os
import urllib.request
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
verze = "version 1.4"


# logo
def logo():
    prGreen("""
    |------|   \     /         |------  |-------|   |\      |   |--------   |-------|   |           |-------
    |      |    \   /          |        |       |   | \     |   |           |       |   |           |
    |      |     \ /           |        |       |   |  \    |   |           |       |   |           |
    |------|      |            |        |       |   |   \   |   |-------|   |       |   |           |-------
    |             |            |        |       |   |    \  |           |   |       |   |           |
    |             |            |        |       |   |     \ |           |   |       |   |           |
    |             |            |------  |-------|   |      \|   --------|   |-------|   |-------    |-------""")


# core(commands)
def core():
    command = input(username + "@local$ ")

    if command == "tisk":
        tisk = input(username + "@local-[tisk]$ ")
        print(tisk)
        core()

    elif command == "pomoc":
        print("""
APP-spustí danou aplikaci
ČAS-ukáže datum a čas
CMD/VERZE-startne nový terminál
CREDITS-credity
HODINY-otevře online hodiny
KOČKA-vytiskne soubor do console
SYSTEM-vypíše informace o systému
TISK-vytiskne input
ODEJIT-odejde
POMOC-pošle příkazy
UPDATE-aktualizuje aplikaci
VYMAZAT-vymaže
            """)
        core()

    elif command == "verze":
        welcome()
        core()

    elif command == "odejit":
        odejit = input("Odejít? [y/n] ")
        print("\n")
        logo()
        time.sleep(2)

        if odejit == "y":
            exit()

        else:
            core()

    elif command == "vymazat":
        try:
            os.system('cls')
            welcome()
            core()

        finally:
            prRed("Jsi na linuxu. Nelze zavírat a otevírat okna. Použij windows.")

    elif command == "sex":
        print("A co sis jako myslel, že se stane")
        core()

    elif command == "cmd":
        print("")
        welcome()
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

    elif command == "ubdate":
        try:
            url = 'https://raw.githubusercontent.com/KralicekGamerCz/py_console/main/PyConsole.py'
            soubor = 'PyConsole.py'
            urllib.request.urlretrieve(url, soubor)
            prRed("Znovu otevři program")
            time.sleep(1)
            exit()

        except:
            prRed("Error")
            core()

    elif command == "credits":
        logo()
        print("\n")
        print("PyConsole byla napsána uživatelem KralicekGamer")
        time.sleep(1.5)
        print("Pár slov autora:")
        time.sleep(1.5)
        print("Toto je můj první project v pythonu a také stávající a na kterém pracuji")
        time.sleep(1.5)
        print("Plánuji udělat KralicekOS nebo PyOS")
        time.sleep(1.5)
        print("Děkuji za podporu a moc si ji vážím")
        print("\n")
        time.sleep(1.5)
        print("KralicekGamer")
        core()

    elif command == "hodiny":
        webbrowser.open_new_tab('clock.html')
        print("Otevírám hodiny\n")
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

    elif command == "čas":
        now = datetime.now()

        print(now.strftime("%d/%m/%Y %H:%M:%S"))

    if command == "app":

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

        elif application == "vulgarism":
            vulgarism = ["blb", "blbina", "blbý", "bordel", "bordel na kolečkách", "bordelmamá", "buzerant", "buzík",
                         "být na dvě věci: na nic a na hovno", "cecek", "cyp", "čubčí", "syn", "čumět", "čurák",
                         "dementi", "do hajzlu", "do piče", "do prdele", "držet držku", "držet hubu", "držet klapačku",
                         "držet kušnu", "držet tlamu", "držet zobák", "flundra", "flus", "frnda", "frňák", "hajtra",
                         "hajzl", "hajzlpapír", "haksna", "hovínko", "hovno", "hovnocuc", "huba", "chcanky", "chcát",
                         "chcípnout", "chlastat", "chuj", "idiot", "jebačka", "jebat", "jít bodnout", "jít do hajzlu",
                         "jít do prdele", "jít vycpat", "kokot", "kokotina", "kretén", "ksindl", "kunda", "kurevník",
                         "kurva", "kurva drát", "kurvafix", "kurvit", "kušna", "lempl", "lofas", "mamrd", "morda",
                         "mrd", "mrdačka", "mrdat", "mrdka", "mrdník", "mrcha", "nasraný", "nasrat", "oddělat",
                         "odkráglovat", "odkrouhnout", "odprásknout", "omrdat", "pajzl", "pazneht", "péro", "piča",
                         "pičus", "pizda", "píča", "píčovina", "píčus", "píchat", "podělaný", "podělat", "pojebaný",
                         "posrat", "prcat", "prd", "prdel", "prdelka", "prdelolezec", "prdět", "prdnout", "prevét",
                         "průser", "přefiknout", "přeříznout", "rozesraný", "rozesrat", "rozmrdaný", "rypák", "sajrajt",
                         "sere pes", "sračka", "sralbotka", "sranec", "sráč", "srágora", "srát", "šoustat", "šuk",
                         "šukačka", "šukat", "šukézní", "šulin", "šulín", "tma jako v prdeli", "trtkat", "ty píčo",
                         "vlezdoprdelista", "vyjebaný", "vyprdnout", "vysrat", "zajebaný", "zasranec", "zásun",
                         "zbouchnout", "zkurvenec", "zkurvený", "zkurvit", "zkurvysyn", "zmrd", "zobák zpíčený", "žrát"]

            print(random.choice(vulgarism))
            core()

        elif application == "pomoc":
                print("""
    KALKULACKA-kalkulačka
    MADLIB-madlib hra
    HESLO-generace hesel
    KÁMEN-NŮŽKY-PAPÍR-kámen nůžky papír hra
    VULGARISM-napíše random vulgarismus
                            """)
                core()

        else:
                prRed("Invalid command")
                core()

    else:
        prRed("Invalid command")
        core()


# run
welcome()
username = input("Username: ")
core()
