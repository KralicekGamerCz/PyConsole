import socket
import platform


def cmd():
    print("\nInformace o systému\n")
    print("Systém: " + platform.system())
    print("Relese: " + platform.release())
    print("Platform version: " + platform.version())
    print("Machine version: " + platform.machine())
    print("Název PC: " + socket.gethostname())
    print("Ip adresa: " + socket.gethostbyname(socket.gethostname()))
    print("Procesor: " + platform.processor() + "\n")
