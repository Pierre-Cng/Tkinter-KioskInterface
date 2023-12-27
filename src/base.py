import tkinter as tk
import background

def on_close():
    pass  # Handle the close event here

def on_ctrl_k(event=None):
    # Close the interface when Ctrl+K is pressed
    root.destroy()

def on_window_resize(event):
    background.set_background(root, "font.png")  

def main():
    global root 
    root = tk.Tk()
    
    # Disable window close button (X button) action
    root.protocol("WM_DELETE_WINDOW", on_close)

    # Maximize the window to full-screen
    root.attributes('-fullscreen', True)

    # Bind Ctrl+K event to close the application
    root.bind('<Control-k>', on_ctrl_k)

    # Configure grid weights to make zones expandable
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=6)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=4)

    icon = background.loading_icon(root)
     
    root.bind("<Configure>", on_window_resize) 
    

    root.mainloop()
    
    root.mainloop()
if __name__ == "__main__":
    main()






