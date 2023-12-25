import tkinter as tk

#def disable_event():
#    pass  # Disable the window close button action

#root = tk.Tk()

# Disable window close button (X button) action
#root.protocol("WM_DELETE_WINDOW", disable_event)

# Maximize the window to full-screen
#root.attributes('-fullscreen', True)

# Create GUI elements
#label = tk.Label(root, text="This is a locked interface")
#label.pack()

# Add more UI elements and functionality as needed

#root.mainloop()


#################



#def on_close():
#    pass  # Handle the close event here

#def on_closing(event=None):
    # Handle Ctrl+C or other custom exit methods
#    root.destroy()

#root = tk.Tk()

# Disable window close button (X button) action
#root.protocol("WM_DELETE_WINDOW", on_close)

# Maximize the window to full-screen
#root.attributes('-fullscreen', True)

# Capture Ctrl+C event to exit the application
#root.bind('<Control-c>', on_closing)

# Create GUI elements
#label = tk.Label(root, text="This is a locked interface")
#label.pack()

# Add more UI elements and functionality as needed

#root.mainloop()

###############################



def on_close():
    pass  # Handle the close event here

def on_ctrl_k(event=None):
    # Close the interface when Ctrl+K is pressed
    #if event.keysym == 'k' and (event.state & 0x4) != 0:  # Check for Ctrl key (0x4)
    root.destroy()

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

# Add more UI elements and functionality as needed

root.mainloop()
