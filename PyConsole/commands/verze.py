from tkinter import messagebox
from commands.etc import system


def cmd():
    messagebox.showinfo("Verze", "PyConsole " + system.verze)
