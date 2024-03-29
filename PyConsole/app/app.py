import string
import random
import __main__
from etc import colors


def cmd():
    application = input(__main__.color_1 + __main__.username + __main__.color_2 + "@" + __main__.color_3 + "local" + colors.yellow + "[app]" + colors.reset + "$ ")
    application = application.replace(" ", "")
    application = application.lower()
    if application == "help":
        print("""
    MATH-kalkulačka
    MADLIB-madlib hra
    PSSWD-generace hesel
    ROCK-PAPER-SCISOURS-kámen nůžky papír hra
                                  """)
        cmd()

    elif application == "math":
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

            else:
                app_madlib()

        app_madlib()

    elif application == "psswd":
        def generate_password(length=8):
            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(characters) for _ in range(length))
            return password

        length = 12
        password = generate_password(length)
        print(f"Vygenerované heslo: {password}")

    elif application == "rockpaperscisors":
        def app_knp():

            app_knp_choices = ["kámen", "nůžky", "papír"]

            app_knp_computer_choice = random.choice(app_knp_choices)

            app_knp_player_choice = input("Kámen, nůžky, nebo papír: ").lower()

            while app_knp_player_choice not in app_knp_choices:
                app_knp_player_choice = input("Kámen, nůžky, nebo papír: ").lower()

            if app_knp_player_choice == app_knp_computer_choice:
                print("Remíza. " + app_knp_player_choice + " x " + app_knp_computer_choice)
            elif app_knp_player_choice == "kámen":
                if app_knp_computer_choice == "nůžky":
                    print("Vyhrál jsi. " + app_knp_player_choice + " x " + app_knp_computer_choice)
                else:
                    print("Prohrál jsi. " + app_knp_player_choice + " x " + app_knp_computer_choice)
            elif app_knp_player_choice == "nůžky":
                if app_knp_computer_choice == "papír":
                    print("Vyhrál jsi. " + app_knp_player_choice + " x " + app_knp_computer_choice)
                else:
                    print("Prohrál jsi.")
            elif app_knp_player_choice == "papír":
                if app_knp_computer_choice == "kámen":
                    print("Vyhrál jsi " + app_knp_player_choice + " x " + app_knp_computer_choice)
                else:
                    print("Prohrál jsi. " + app_knp_player_choice + " x " + app_knp_computer_choice)
            app_knp_pa_vyber = input("Hrát znovu? [y/n] ")
            if app_knp_pa_vyber == "y":
                app_knp()

        app_knp()

    else:
        print(colors.red + "Invalid command\n")
