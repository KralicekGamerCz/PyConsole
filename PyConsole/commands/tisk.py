import __main__
from commands.etc import colors


def cmd():
    cmd_tisk_content = input("\033[94m" + __main__.username + "\033[35m" + "@" + colors.green + "local" + "" + "\033[33m" + "[tisk]" + colors.reset + "$ ")
    print(cmd_tisk_content)
