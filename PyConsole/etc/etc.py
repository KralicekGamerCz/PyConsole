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
verze = "version pre-relese 2.0 windows"


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
