import tkinter as tk

from gui.widgets import side_menu


def run():
    root = tk.Tk()
    root.title("Betting Tool")
    root.configure(background="#060e1f")
    root.geometry("500x500")

    menu_button = side_menu.Menu_Button(root)
    menu_button.grid(row=0, column=0, padx=10, pady=10)


    root.mainloop()
