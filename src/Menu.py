import tkinter as tk
from tkinter import ttk
from tkinter import font as tkfont
from Stopwatch import Stopwatch 

class Menu:
    def __init__(self, root):
        # Initial setting
        self.root = root
        self.set_frame()
        self.set_font()
        # Vehicule choice
        self.combos = {}
        self.combos['category'] = self.add_combo(column=0)
        self.combos['number'] = self.add_combo(column=1)
        self.add_spacer(2, 3)
        # Configuration choice 
        self.verify_button = self.add_button('Verify Configuration', column=3)
        self.config_label = self.add_label(column=4)
        self.config_button = self.add_button('Modify Configuration', column=5) 
        self.add_spacer(6, 3)
        # Recording logs 
        self.recording_button = self.add_button('Start Recording', bg='green', column=7)
        self.stopwatch = Stopwatch(self.frame, self.text_font, column=8)
        self.send_button = self.add_button('Send Data', column=9)
    
    def set_font(self):
        self.button_font = tkfont.Font(family='Trebuchet MS', size=12) 
        self.text_font = tkfont.Font(family='Trebuchet MS', size=12)

    def set_frame(self):
        self.frame = tk.Frame(self.root)
        self.frame.configure(bg='#111333', padx=20, pady=10)
        self.frame.pack(fill='both', expand=False)

    def add_combo(self, option_list=[], row=0, column=0):
        # Create and position a dropdown list (combobox) on the top left corner
        combo = ttk.Combobox(self.frame, values=option_list, font=self.text_font)
        self.frame.grid_columnconfigure(column, weight=1)
        combo.grid(row=row, column=column, sticky="nsew", padx=10, pady=10)
        return combo
    
    def add_button(self, text, bg='lightgrey', row=0, column=0):
        button = tk.Button(self.frame, text=text, borderwidth=4, bg=bg, font=self.button_font)
        self.frame.grid_columnconfigure(column, weight=1)
        button.grid(row=row, column=column, sticky="nsew", padx=10, pady=10)
        return button
    
    def add_label(self, text='', row=0, column=0):
        label = tk.Label(self.frame, text=text, borderwidth=1, relief="solid", justify="center", font=self.text_font, width=30, height=4, anchor='n')
        self.frame.grid_columnconfigure(column, weight=2)
        label.grid(row=row, column=column, sticky="nsew", padx=10, pady=10)
        return label
        
    def add_spacer(self, column, weight):
        self.frame.grid_columnconfigure(column, weight=weight)
