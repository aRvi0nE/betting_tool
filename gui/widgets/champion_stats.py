import tkinter as tk
from tkinter import ttk


class Window(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Champion Stats")
        self.geometry("1000x800")
        self.configure(background="#060e1f")

        self.label_frame1 = tk.LabelFrame(self, bg="#060e1f", height=571)
        self.label_frame2 = tk.LabelFrame(self, bg="#060e1f")

        self.canvas = tk.Canvas(self.label_frame1, bg="#060e1f", borderwidth=0, highlightthickness=0, height=571)

        self.scrollbar_vertical = ttk.Scrollbar(self.label_frame1, orient="vertical", command=self.canvas.yview)
        self.scrollbar_vertical.pack(side=tk.RIGHT, fill=tk.Y)
        self.scrollbar_horizontal = ttk.Scrollbar(self.label_frame1, orient="horizontal", command=self.canvas.xview)
        self.scrollbar_horizontal.pack(side=tk.BOTTOM, fill=tk.X)
        self.canvas.configure(yscrollcommand=self.scrollbar_vertical.set, xscrollcommand=self.scrollbar_horizontal.set)
        self.canvas.bind('<Configure>', lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.frame = tk.Frame(self.canvas, bg="#060e1f", borderwidth=0)
        self.canvas.create_window((0, 0), window=self.frame, anchor="nw")

        self.table = tk.PhotoImage(file="gui/assets/graphs/table.png")
        self.label = tk.Label(self.frame, image=self.table, borderwidth=0, width=self.table.width()-2, height=self.table.height()-2)
        self.label.grid(row=0, column=0, sticky="nw")
        self.canvas.pack(side="left", anchor="nw", fill="x")

        self.label_frame1.pack(fill="both", expand="no", padx=20)
        self.label_frame2.pack(fill="both", expand="yes", padx=20)
