from PyConsole.commands.etc import colors

username = "test"

barva_1 = colors.lightblue
barva_2 = colors.purple
barva_3 = colors.green

while True:
    command = input(barva_1 + username + barva_2 + "@" + barva_3 + "testing" + colors.reset + "$ ")
    command = command.replace(" ", "")
    command = command.lower()

    if command == "editcolors":
        print("""
Zde jsou dostupné barvy:
black
red
green 
orange 
blue
purple 
cyan
lightgrey
darkgrey
lightred
lightgreen
yellow
lightblue 
pink 
lightcyan 
""")
        barva_1_custom = input("1. barva: ")
        barva_2_custom = input("2. barva: ")
        barva_3_custom = input("3. barva: ")

        barva_1 = getattr(colors, barva_1_custom, colors.lightblue)
        barva_2 = getattr(colors, barva_2_custom, colors.purple)
        barva_3 = getattr(colors, barva_3_custom, colors.green)

    elif command == "colorsreset":
        barva_1 = colors.lightblue
        barva_2 = colors.purple
        barva_3 = colors.green
        print("Barvy resetovány")

    elif command == "exit":
        exit()

    else:
        print("Test")
