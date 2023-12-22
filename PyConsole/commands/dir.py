import os


def cmd():
    def list_directory_contents(directory):
        try:
            contents = os.listdir(directory)
            for item in contents:
                print(item)
        except FileNotFoundError:
            print("Složka neexistuje.")
        except NotADirectoryError:
            print("Zadaná cesta není složka.")

    folder_path = input("Adresa složky: ")

    list_directory_contents(folder_path)
