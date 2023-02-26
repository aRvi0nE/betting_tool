import tkinter as tk
import gui
from gui.widgets import champion_stats

menu_is_on = False


class Menu_Button(tk.Button):
    def __init__(self, master):
        super().__init__()
        self.menu_button_image = tk.PhotoImage(file="gui/assets/menu_button.png")
        self.configure(image=self.menu_button_image,
                       width=40,
                       height=40,
                       borderwidth=0,
                       highlightthickness=0,
                       relief=tk.RAISED,
                       command=lambda: self.menu_button_action(master))

    def menu_button_action(self, master):
        global menu_is_on
        global menu
        if not menu_is_on:
            self.grid(row=0, column=1, stick="N")
            menu = Menu(master)
            master.rowconfigure(0, weight=1)
            menu.grid(row=0, column=0, sticky="NSW")
            menu_is_on = True
        else:
            menu.destroy()
            self.grid(row=0, column=0, stick="N")
            menu_is_on = False


class Menu(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(bg="#07213a")

        champion_stats_button = tk.Button(self, text="Champion Stats", bg="#01080f", fg="#c0aa73", command=self.open_champion_stats)
        team_stats_button = tk.Button(self, text="Team Stats", bg="#01080f", fg="#c0aa73")

        champion_stats_button.grid(row=1, column=2, sticky="w", padx=10, pady=[10, 3])
        team_stats_button.grid(row=2, column=2, sticky="w", padx=10, pady=3)

    @staticmethod
    def open_champion_stats():
        top = champion_stats.Window()

