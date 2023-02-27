# Pyton konzole
# Napsal KralicekGamer
# Zákaz jekéhokoli kopírování vydávání za vlastní atd.
import string
import random
import shutil
import time
import sys

print("""
    Vítej v této konzoly
    Napiš "pomoc" pro help
    ©2023 by KralicekGamer
""")


def core():
    command = input(">>> ")

    if command == "tisk":
        tisk = input("  >>> ")
        print(tisk)
        core()

    if command == "pomoc":
        print("""
    Vítej v této konzoly
    Toto je konzole dělaná na windows powershell
            
    TISK-vytiskne input
    POMOC-pošle příkazy
    UBDATE-napíše update
    ODEJIT-odejde
    VYMAZAT-vymaže
    CMD-startne nový terminál
    APP-spustí danou aplikaci
            """)
        core()

    if command == "ubdate":
        print("""
            Update 1.1
            -Přídány commandy
            -Přidány aplikace
            """)
        core()

    if command == "odejit":
        print("Exitting program")
        exit()

    if command == "vymazat":
        print("""
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
            """)
        core()

    if command == "sex":
        print("A co sis jako myslel, že se stane")
        core()

    if command == "cmd":
        print("""
    Vítej v této konzoly
    Napiš "pomoc" pro help
    ©2023 by KralicekGamer
            """)
        core()

    if command == "matrix":
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

    if command == "app":
        application = input("  >>> ")

        if application == "kalkulacka":
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

        if application == "madlib":
            secret_world = input("Create secret world: ")

            def madlib():
                guess = input("Enter guess: ")

                if guess == secret_world:
                    print("You win")
                    core()

                else:
                    madlib()

            madlib()

        if application == "heslo":
            length = int(input("Délka hesla: "))

            print('''Zde vyber, co chceš mít v hesle za znaky
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

        if application == "kámen-nůžky-papír":
            def kamen_nuzky_papir():

                choices = ["kámen", "nůžky", "papír"]

                computer_choice = random.choice(choices)

                player_choice = input("Kámen, nůžky, nebo papír: ").lower()

                while player_choice not in choices:
                    player_choice = input("Kámen, nůžky, nebo papír: ").lower()

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

                core()

            kamen_nuzky_papir()

        if application == "pomoc":
            print("""
    KALKULACKA-kalkulačka
    MADLIB-madlib hra
    HESLO-generace hesel
    KÁMEN-NŮŽKY-PAPÍR-kámen nůžky papír hra
                        """)
            core()

        else:
            print("Invalid command")
            core()

    else:
        print("Invalid command")
        core()

core()
