import tkinter as tk
import json
from tkinter import ttk
from Configurator import Configurator
from tkinter import messagebox
import time
class Popup:
    def __init__(self, root):
        self.root = root
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
            combo = ttk.Combobox(self.device_frame, values=['a', 'b', 'c'], width=5) # ajust with dbc list 
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
