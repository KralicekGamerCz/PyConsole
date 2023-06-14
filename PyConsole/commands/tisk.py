import __main__
from etc import etc


def cmd():
    cmd_tisk_content = input("\033[94m" + __main__.username + "\033[35m" + "@" + etc.green + "local" + "" + "\033[33m" + "[tisk]" + etc.reset + "$ ")
    print(cmd_tisk_content)
