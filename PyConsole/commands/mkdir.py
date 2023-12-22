import os


def cmd():
    mk_dir_directory_name = input("Název složky: ")
    os.mkdir(mk_dir_directory_name)
    print("")
