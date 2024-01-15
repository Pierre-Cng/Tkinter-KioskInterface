from Configurator import Configurator
import tkinter as tk 
import json
from tkinter import ttk
from tkinter import messagebox
from SshClient import SshClient
from Popup import Popup
class Actions:
    def __init__(self, root, menu, content, footer):
        self.config_verified = False
        self.root = root 
        self.menu = menu 
        self.content = content 
        self.footer = footer
        self.configurator = Configurator()
        self.configure_combos()
        self.configure_buttons()
        self.configure_label()

    def configure_combos(self):
        self.combo_choices = {}
        self.menu.combos['category'].config(values=self.configurator.data['Combos']['Category'])
        self.menu.combos['number'].config(values=self.configurator.data['Combos']['Number'])
        self.menu.combos['category'].current(0)
        self.menu.combos['number'].current(0)
        self.menu.combos['category'].bind('<<ComboboxSelected>>', lambda event, arg='category': self.on_combo_change(event, arg))
        self.menu.combos['number'].bind('<<ComboboxSelected>>', lambda event, arg='number': self.on_combo_change(event, arg))

    def configure_buttons(self):
        self.menu.verify_button.config(command=self.verify_config)
        self.menu.config_button.config(command=self.modify_config)
        self.menu.recording_button.config(command=self.start_recording)
        self.menu.send_button.config(command=self.send_data)

    def configure_label(self):
        self.menu.config_label.config(text=self.configurator.displayed_config_info())

    def on_combo_change(self, event, comboID):
        self.combo_choices[comboID] = self.menu.combos[comboID].get()

    def verify_config(self):
        self.configurator.get_config_backup()
        self.configure_label() 
        self.config_verified = True

    def modify_config(self):
        #self.create_popup()
        popup = tk.Toplevel(self.root)
        content = Popup(popup)
        # open pop up with list of available stack and available dbc - allow user to associate them together 
        # option to refresh dbc and stack and fetch latest 
        # update config label 

    def start_recording(self):
        # Verify if combos and config have been set
        if len(self.combo_choices)<1:
            messagebox.showinfo("Warning", "Please select a vehicle category and number.")
            return
        if not self.config_verified:
            messagebox.showinfo("Warning", "Please verify the config before recording.")
            return
        # Stopwatch
        self.menu.stopwatch.start_stopwatch()
        # Start command 

        # launch script for stack to record - lauch oscilloscope 
        self.content.graph.switch_oscilloscope()
        self.menu.recording_button.config(text="Stop Recording", command=self.stop_recording, bg='red')
        print(self.content.check_list.clicked_list)
        #execute_bash_script()

    def stop_recording(self):
        # lauch script to save logs and stop stack - stop stopwatch - stop oscilloscope - allow send data button  
        self.menu.stopwatch.stop_stopwatch()
        self.content.graph.switch_oscilloscope()
        self.menu.recording_button.config(text="Start Recording", command=self.start_recording, bg='green')
        
    def send_data(self):
        pass
    # when allowed send recorded logs under vehicule + number file name to s3 server 
