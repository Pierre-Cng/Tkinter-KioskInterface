import tkinter as tk
import subprocess

def on_close():
    pass  # Handle the close event here

def on_ctrl_k(event=None):
    # Close the interface when Ctrl+K is pressed
    root.destroy()

def execute_bash_script():
    # Execute a Bash script when the button is clicked
    subprocess.run(['py','dummy.py'])  # Replace with your script path

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
button = tk.Button(root, text="Run Bash Script", command=execute_bash_script)
button.pack()

# Add more UI elements and functionality as needed

root.mainloop()