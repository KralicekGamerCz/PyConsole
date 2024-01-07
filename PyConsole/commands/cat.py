def cmd():
    def cat(file_path):
        try:
            with open(file_path, "r") as file:
                content = file.read()
                print(content)
        except FileNotFoundError:
            print("Soubor neexistuje.")

    file_path = input("Zadejte cestu k souboru: ")
    cat(file_path)
