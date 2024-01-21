import tkinter as tk
from tkinter import ttk
from tkinter import font as tkfont
from tkinter import messagebox
import json
from Widget import Stopwatch, Oscilloscope, TreeCheckList
from ComManager import Configurator
from Actions import Actions

class App:
    def __init__(self, root):
        self.root = root
        self.configure_kiosk_style()
        self.Menu = Menu(self.root)
        self.Content = Content(self.root)
        self.Footer = Footer(self.root)
        self.Popup = Popup(self.root)
        self.Actions = Actions(self.root, self.Menu, self.Content, self.Footer, self.Popup)

    def on_close(self):
        pass  # Handle the close event here

    def on_ctrl_k(self, event=None):
        # Close the interface when Ctrl+K is pressed
        self.root.quit()

    def configure_kiosk_style(self):
        # Disable window close button (X button) action
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        # Maximize the window to full-screen
        self.root.attributes('-fullscreen', True)
        # Bind Ctrl+K event to close the application
        self.root.bind('<Control-k>', self.on_ctrl_k)

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
        self.verify_button = self.add_button('Verify Connection', column=3)
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

class Content:
    def __init__(self, root):
        self.root = root
        self.set_frame()
        self.set_tree()
        self.graph = Oscilloscope(self.frame)
    
    def set_frame(self):
        self.frame = tk.Frame(self.root)
        self.frame.configure(padx=20, pady=50)
        self.frame.pack(fill="both", expand=False)

    def set_tree(self):
        self.tree = TreeCheckList(self.frame)
        self.frame.grid_columnconfigure(0, weight=1)
        self.tree.grid(row=0, column=0, sticky="nsew", padx=30, pady=10)

class Footer(Menu):
    def __init__(self, root):
        self.root = root
        self.set_frame()
        self.set_font()
        self.add_spacer(column=0, weight=4)
        self.jira_button = self.add_button('Create a Jira Ticket', 'darkred', column=4)

    def set_frame(self):
        self.frame = tk.Frame(self.root)
        self.frame.configure(bg='#111333', padx=20, pady=20)
        self.frame.pack(side='bottom', fill='both', expand=False)

class Popup:
    def __init__(self, root):
        self.root = root

    def activate(self):
        self.root = tk.Toplevel(self.root)
        self.dbc_list = ['a', 'b', 'c']
        #self.devices_list = Configurator().list_connected_devices()
        self.devices_list = ['test', 'test']
        self.layout()
        self.combo_values = ["Val 1", "Val 2", "Val 3", "Val 4"]  # List to store ComboBox values #use on combo change

    def layout(self):
        self.root.title("Configuration pannel")
        self.root.geometry("300x400")  # Set main window size
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(2, weight=1)
        device_button = tk.Button(self.root, text="Search for connected devices", command=self.display_devices)
        device_button.grid(row=0, column=1, padx=5, pady=5)
        section_title = tk.Label(self.root, text="Devices found:")
        section_title.grid(row=1, column=1, padx=5, pady=5)
        self.device_frame = tk.Frame(self.root, bg='white', width=200, height=250, highlightbackground="black", highlightthickness=1)
        self.device_frame.grid_propagate(False)  # Prevent frame from resizing based on content
        self.device_frame.grid(row=2, column=1, padx=10, pady=10, sticky='news')
        save_button = tk.Button(self.root, text="Save and Configure", command=self.save_and_configure)
        save_button.grid(row=3, column=1, padx=5, pady=5)

    def display_devices(self):
        for i, device in enumerate(self.devices_list):
            label = tk.Label(self.device_frame, text=device)
            label.grid(row=i, column=1, padx=5, pady=5, sticky='w')
            combo = ttk.Combobox(self.device_frame, values=self.dbc_list, width=5) # ajust with dbc list 
            combo.set('a')  # Set default choice to 'a'
            combo.grid(row=i, column=2, padx=5, pady=5, sticky='e')

    def save_and_configure(self):
        with open('devices_config.json', 'r') as file:
            data = json.load(file)
        for i, device in enumerate(self.devices_list):
            data[device] = self.combo_values[i]
        with open('devices_config.json', 'w') as file:
            json.dump(data, file, indent=4)  
        msg = messagebox.showinfo("Information", "Your configuration has been saved.")
        self.root.destroy()
