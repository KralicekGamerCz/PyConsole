import os


def cmd():
    rm_dir_directory_name = input("Název složky: ")
    os.rmdir(rm_dir_directory_name)
    print("")
