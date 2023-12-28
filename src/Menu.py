import tkinter as tk
from tkinter import ttk
import time 

category_list = ['A','B']
number_list = ['1', '2']
        
class Menu:
    def __init__(self, root):
        self.root = root
        self.set_frame()
        self.category_combo = self.add_combo(category_list, column=0)
        self.number_combo = self.add_combo(number_list, column=1)
        self.add_recording_button()
        self.add_stopwatch()
        
    def set_frame(self):
        self.frame = tk.Frame(self.root)
        self.frame.grid(row=0, column=0, sticky="nw")

    def add_combo(self, option_list, row=0, column=0):
        # Create and position a dropdown list (combobox) on the top left corner
        combo = ttk.Combobox(self.frame, values=option_list)
        combo.current(0)  # Set the default selected option
        combo.grid(row=row, column=column, sticky="nw", padx=5, pady=5)
        return combo
    
    def add_recording_button(self):
        self.recording_button = tk.Button(self.frame, text="Start Recording", command=self.start_recording, bg='green')
        self.recording_button.grid(row=0, column=2, sticky="nw", padx=5, pady=5)
    
    def start_recording(self):
        # Function to start recording - Change the button appearance and functionality
        self.start_stopwatch()
        self.recording_button.config(text="Stop Recording", command=self.stop_recording, bg='red')

    def stop_recording(self):
        # Function to stop recording - Change the button appearance and functionality
        self.stop_stopwatch()
        self.recording_button.config(text="Start Recording", command=self.start_recording, bg='green')
        #execute_bash_script()
    
    def add_stopwatch(self):
        self.start_time = None
        self.stopwatch_running = False
        self.time_label = tk.Label(self.frame, text="00:00:00")
        self.time_label.grid(row=0, column=3, sticky="nw", padx=5, pady=5)

    def start_stopwatch(self):
        if self.start_time is not None:
            self.reset_stopwatch()
        self.stopwatch_running = True
        self.start_time = time.time() 
        self.update_time()

    def stop_stopwatch(self):
        self.stopwatch_running = False

    def update_time(self):
        if self.stopwatch_running:
            elapsed_time = time.time() - self.start_time
            hours = int(elapsed_time // 3600)
            minutes = int((elapsed_time % 3600) // 60)
            seconds = int(elapsed_time % 60)
            time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            self.time_label.config(text=time_str)
        self.time_label.after(1000, self.update_time)

    def reset_stopwatch(self):
        self.time_label.config(text="00:00:00")


    

    

    

    