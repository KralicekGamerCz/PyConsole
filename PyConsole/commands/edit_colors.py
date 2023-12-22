from etc import colors
import __main__


def cmd():
    print("""
Zde jsou dostupné barvy:
black, red, green, orange, blue, purple, cyan, lightgrey, darkgrey, lightred, lightgreen, yellow, lightblue, pink, lightcyan 
""")
    barva_1_custom = input("1. barva: ")
    barva_2_custom = input("2. barva: ")
    barva_3_custom = input("3. barva: ")

    __main__.barva_1 = getattr(colors, barva_1_custom, colors.lightblue)
    __main__.barva_2 = getattr(colors, barva_2_custom, colors.purple)
    __main__.barva_3 = getattr(colors, barva_3_custom, colors.green)
