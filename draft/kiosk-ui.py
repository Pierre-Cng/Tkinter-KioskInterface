'''

def execute_bash_script():
    # Execute a Bash script when the button is clicked
    subprocess.run(['py','dummy.py'])  # Replace with your script path

# Button to execute the Bash script
button = tk.Button(root, text="Run Bash Script", command=execute_bash_script, bg='green', fg='white', font=('Arial', 20))
button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
button.config(width=15, height=3)  # Adjust button size

# Functionality to change button appearance and function on click
button.config(command=start_recording)

'''

############################

import tkinter as tk
from tkinter import IntVar
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import pandas as pd

def on_close():
    pass  # Handle the close event here

def on_ctrl_k(event=None):
    # Close the interface when Ctrl+K is pressed
    root.destroy()

def start_recording():
    # Function to start recording - Change the button appearance and functionality
    button.config(text="Stop Recording", command=stop_recording, bg='red')

def stop_recording():
    # Function to stop recording - Change the button appearance and functionality
    button.config(text="Start Recording", command=start_recording, bg='green')

def execute_bash_script():
    # Execute a Bash script when the button is clicked
    # subprocess.run(["/bin/bash", "/path/to/your/script.sh"])  # Replace with your script path
    pass

def plot_graph():
    # Read CSV data and plot a graph
    data1 = pd.read_csv('output1.csv')  # Replace with your CSV file path
    data2 = pd.read_csv('output2.csv') 
    plt.figure(figsize=(6, 4))  # Adjust the figure size as needed
    plt.plot(data1['x'], data1['y'])  # Assuming 'x' and 'y' are column headers in your CSV
    plt.plot(data2['x'], data2['y'])
    plt.xlabel('X-axis Label')
    plt.ylabel('Y-axis Label')
    plt.title('Graph Title')
    plt.grid(True)
    
    # Embed the plot into Tkinter window
    canvas = FigureCanvasTkAgg(plt.gcf(), master=root)
    canvas.draw()
    canvas.get_tk_widget().place(relx=0.5, rely=0.5, anchor=tk.CENTER)

root = tk.Tk()

# Disable window close button (X button) action
root.protocol("WM_DELETE_WINDOW", on_close)

# Maximize the window to full-screen
root.attributes('-fullscreen', True)

# Bind Ctrl+K event to close the application
root.bind('<Control-k>', on_ctrl_k)

# Create GUI elements
label = tk.Label(root, text="This is a locked interface")
label.pack()

# Button to execute the Bash script
button = tk.Button(root, text="Run Bash Script", command=execute_bash_script, bg='green', fg='white', font=('Arial', 20))
button.place(x=10, y=10)  
button.config(width=15, height=3)  # Adjust button size

# Functionality to change button appearance and function on click
button.config(command=start_recording)

# Button to plot the graph
#plot_button = tk.Button(root, text="Plot Graph", command=plot_graph)
#plot_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
plot_graph()
# Add more UI elements and functionality as needed

# Checkable options for the graph placed on the left
options_frame = tk.Frame(root)
options_frame.place(relx=0.1, rely=0.5, anchor=tk.W)

check_var1 = IntVar()
check_var2 = IntVar()
check_var3 = IntVar()

check1 = tk.Checkbutton(options_frame, text="Option 1", variable=check_var1)
check1.pack(anchor=tk.W)

check2 = tk.Checkbutton(options_frame, text="Option 2", variable=check_var2)
check2.pack(anchor=tk.W)

check3 = tk.Checkbutton(options_frame, text="Option 3", variable=check_var3)
check3.pack(anchor=tk.W)


root.mainloop()
