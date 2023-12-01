import tkinter as tk
from tkinter import filedialog, messagebox
from etc import colors


def cmd():
    print(colors.red + "Textový editor je otevřen")

    class TextEditor:
        def __init__(self):
            self.root = root
            self.root.title("PyConsole text editor")

            self.text_area = tk.Text(self.root)
            self.text_area.pack(fill=tk.BOTH, expand=True)

            self.menu_bar = tk.Menu(self.root)
            self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
            self.file_menu.add_command(label="Otevřít", command=self.cmd_open_file)
            self.file_menu.add_command(label="Uložit", command=self.cmd_save_file)
            self.file_menu.add_command(label="Uložit jako", command=self.cmd_save_file_as)
            self.file_menu.add_separator()
            self.file_menu.add_command(label="Konec", command=self.cmd_exit)
            self.menu_bar.add_cascade(label="Soubor", menu=self.file_menu)

            self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
            self.edit_menu.add_command(label="Vyjmout", command=self.cmd_cut)
            self.edit_menu.add_command(label="Kopírovat", command=self.cmd_copy)
            self.edit_menu.add_command(label="Vložit", command=self.cmd_paste)
            self.menu_bar.add_cascade(label="Úpravy", menu=self.edit_menu)

            self.help_menu = tk.Menu(self.menu_bar, tearoff=0)
            self.help_menu.add_command(label="O programu", command=self.cmd_version)
            self.menu_bar.add_cascade(label="Nápověda", menu=self.help_menu)

            self.root.config(menu=self.menu_bar)

        def cmd_open_file(self):
            file_path = filedialog.askopenfilename(filetypes=[("Textové soubory", "*.txt")])
            if file_path:
                try:
                    with open(file_path, "r") as cmd_text_file:
                        self.text_area.delete("1.0", tk.END)
                        self.text_area.insert(tk.END, cmd_text_file.read())
                except Exception as e:
                    messagebox.showerror("Chyba", str(e))

        def cmd_save_file(self):
            file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Textové soubory", "*.txt")])
            if file_path:
                try:
                    with open(file_path, "w") as cmd_text_file:
                        cmd_text_file.write(self.text_area.get("1.0", tk.END))
                except Exception as e:
                    messagebox.showerror("Chyba", str(e))

        def cmd_save_file_as(self):
            file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Textové soubory", "*.txt")])
            if file_path:
                try:
                    with open(file_path, "w") as cmd_text_file:
                        cmd_text_file.write(self.text_area.get("1.0", tk.END))
                except Exception as e:
                    messagebox.showerror("Chyba", str(e))

        def cmd_exit(self):
            self.root.quit()

        def cmd_cut(self):
            self.text_area.event_generate("<<Cut>>")

        def cmd_copy(self):
            self.text_area.event_generate("<<Copy>>")

        def cmd_paste(self):
            self.text_area.event_generate("<<Paste>>")

        @staticmethod
        def cmd_version():
            messagebox.showinfo("O programu", "Version 3.0")

    root = tk.Tk()
    TextEditor()
    root.mainloop()
    print("")
