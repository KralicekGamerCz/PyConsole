# PyConsole
# Version 1.3
# ©2023 by KralicekGamer


import string
import random
import shutil
import time
import sys
import os
import urllib.request


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
    print("PyConsole [Version 1.3] \n©2023 by KralicekGamer\n")


# core(commands)
def core():
    command = input(">>> ")

    if command == "tisk":
        tisk = input("  >>> ")
        print(tisk)
        core()

    elif command == "pomoc":
        print("""
APP-spustí danou aplikaci
CMD/VERZE-startne nový terminál
KOČKA-vytiskne soubor do console
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

        if odejit == "y":
            exit()

        else:
            core()

    elif command == "vymazat":
        os.system('cls')
        welcome()
        core()

    elif command == "sex":
        print("A co sis jako myslel, že se stane")
        core()

    elif command == "cmd":
        print("")
        welcome()
        core()

    elif command == "matrix":
        # ! /usr/bin/env python3

        # Author: Joao S. O. Bueno
        # gwidion@gmail.com
        # GPL. v3.0

        MAX_CASCADES = 600
        MAX_COLS = 20
        FRAME_DELAY = 0.03

        MAX_SPEED = 5

        from random import choice, randrange, paretovariate

        CSI = "\x1b["
        pr = lambda command: print("\x1b[", command, sep="", end="")
        getchars = lambda start, end: [chr(i) for i in range(start, end)]

        black, green, white = "30", "32", "37"

        latin = getchars(0x30, 0x80)
        greek = getchars(0x390, 0x3d0)
        hebrew = getchars(0x5d0, 0x5eb)
        cyrillic = getchars(0x400, 0x50)

        chars = latin + greek + hebrew + cyrillic

        def pareto(limit):
            scale = lines // 2
            number = (paretovariate(1.16) - 1) * scale
            return max(0, limit - number)

        def init():
            global cols, lines
            cols, lines = shutil.get_terminal_size()
            pr("?25l")  # Hides cursor
            pr("s")  # Saves cursor position

        def end():
            pr("m")  # reset attributes
            pr("2J")  # clear screen
            pr("u")  # Restores cursor position
            pr("?25h")  # Show cursor

        def print_at(char, x, y, color="", bright="0"):
            pr("%d;%df" % (y, x))
            pr(bright + ";" + color + "m")
            print(char, end="", flush=True)

        def update_line(speed, counter, line):
            counter += 1
            if counter >= speed:
                line += 1
                counter = 0
            return counter, line

        def cascade(col):
            speed = randrange(1, MAX_SPEED)
            espeed = randrange(1, MAX_SPEED)
            line = counter = ecounter = 0
            oldline = eline = -1
            erasing = False
            bright = "1"
            limit = pareto(lines)
            while True:
                counter, line = update_line(speed, counter, line)
                if randrange(10 * speed) < 1:
                    bright = "0"
                if line > 1 and line <= limit and oldline != line:
                    print_at(choice(chars), col, line - 1, green, bright)
                if line < limit:
                    print_at(choice(chars), col, line, white, "1")
                if erasing:
                    ecounter, eline = update_line(espeed, ecounter, eline)
                    print_at(" ", col, eline, black)
                else:
                    erasing = randrange(line + 1) > (lines / 2)
                    eline = 0
                yield None
                oldline = line
                if eline >= limit:
                    print_at(" ", col, oldline, black)
                    break

        def main():
            cascading = set()
            added_new = True
            while True:
                while add_new(cascading): pass
                stopped = iterate(cascading)
                sys.stdout.flush()
                cascading.difference_update(stopped)
                time.sleep(FRAME_DELAY)

        def add_new(cascading):
            if randrange(MAX_CASCADES + 1) > len(cascading):
                col = randrange(cols)
                for i in range(randrange(MAX_COLS)):
                    cascading.add(cascade((col + i) % cols))
                return True
            return False

        def iterate(cascading):
            stopped = set()
            for c in cascading:
                try:
                    next(c)
                except StopIteration:
                    stopped.add(c)
            return stopped

        def doit():
            try:
                init()
                main()
            except KeyboardInterrupt:
                pass
            finally:
                end()

        if __name__ == "__main__":
            doit()

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
            prRed("Invalid file name")
            core()

    elif command == "update":
        url = 'https://raw.githubusercontent.com/KralicekGamerCz/py_console/main/run.py'
        soubor = 'run.py'
        urllib.request.urlretrieve(url, soubor)
        prRed("Znovu otevři program")
        time.sleep(1)
        exit()

    if command == "app":

        application = input("  >>> ")

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
core()

