import tkinter as tk
from tkinter import ttk
import subprocess
import os
import time 

category_list = ['A','B']
number_list = ['1', '2']
        
class Menu:
    def __init__(self, root):
        self.root = root
        self.set_frame()
        self.category_combo = self.add_combo(category_list)
        self.number_combo = self.add_combo(number_list)
        
    def set_frame(self):
        self.frame = tk.Frame(self.root)
        self.frame.grid(row=0, column=0, sticky="nw")

    def add_combo(self, option_list):
        # Create and position a dropdown list (combobox) on the top left corner
        combo = ttk.Combobox(self.root, values=option_list)
        combo.current(0)  # Set the default selected option
        combo.pack(side="left", padx=5, pady=5, fill="x", expand=True)
        return combo
    
######################
'''

def start_timer():
    start_time = time.time()
    update_timer(start_time)

def update_timer(start_time):
    elapsed_time = time.time() - start_time
    timer_label.config(text=f"Elapsed Time: {elapsed_time:.2f} seconds")
    root.after(100, self.update_timer)

def add_dropdowns(root):
    #combo_frame = tk.Frame(root)
    #combo_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

    # Create and position the first dropdown list (combobox) on the top left corner
    combo1 = ttk.Combobox(root, values=["Option 1", "Option 2", "Option 3"])
    combo1.current(0)  # Set the default selected option
    #combo1.pack(side="top", padx=5, pady=5)
    combo1.pack(side="left", padx=5, pady=5, fill="x", expand=True)

    # Create and position the second dropdown list (combobox) below the first one
    combo2 = ttk.Combobox(root, values=["A", "B", "C"])
    combo2.current(0)  # Set the default selected option
    #combo2.pack(side="top", padx=5, pady=5)
    combo2.pack(side="left", padx=5, pady=5, fill="x", expand=True)

    global timer_label
    timer_label = tk.Label(root, text="Elapsed Time: 0 seconds")
    timer_label.pack(side="right", padx=5, pady=5)

    button = tk.Button(root, text="Start", command=start_timer)
    button.pack(side="right", padx=5, pady=5)

    

def start_recording():
    # Function to start recording - Change the button appearance and functionality
    button.config(text="Stop Recording", command=stop_recording, bg='red')

def stop_recording():
    # Function to stop recording - Change the button appearance and functionality
    button.config(text="Start Recording", command=start_recording, bg='green')
    execute_bash_script()

def execute_bash_script():
    # Execute a Bash script when the button is clicked
    subprocess.run(['py',os.path.join(os.getcwd(), r'src\dummy_process.py')])  # Replace with your script path

def add_recording_button(root):
    # Button to execute the Bash script
    global button
    button = tk.Button(root, text="Run Bash Script", command=start_recording, bg='green', fg='white', font=('Arial', 20))
    button.pack(side="right", padx=5, pady=5) 
    button.config(width=10, height=2)  # Adjust button size
    return button

'''