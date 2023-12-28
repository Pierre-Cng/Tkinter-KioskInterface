import tkinter as tk
from PIL import Image, ImageTk

def on_close():
    pass  # Handle the close event here

def on_ctrl_k(event=None):
    # Close the interface when Ctrl+K is pressed
    root.destroy()

def create_zone(parent, row, column, rowspan=1, columnspan=1, color="white"):
    zone = tk.Frame(parent, bg=color, highlightbackground="darkgrey", highlightthickness=2)
    zone.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan, sticky="nsew")
    return zone

def add_widgets_to_zone(zone, label_text):
    label = tk.Label(zone, text=label_text, font=("Arial", 12), padx=10, pady=10)
    label.pack(expand=True)

def set_resized_background(root, image_path):
    # Open and resize the image to fit the window
    image = Image.open(image_path)
    window_width = root.winfo_width()
    window_height = root.winfo_height()
    resized_image = image.resize((window_width, window_height))

    # Convert the resized image to PhotoImage
    photo = ImageTk.PhotoImage(resized_image)
    
    # Set the resized image as background
    label = tk.Label(root, image=photo)
    label.image = photo  # To prevent image garbage collection
    label.place(x=0, y=0, relwidth=1, relheight=1)

def on_window_resize(event):
    set_resized_background(root, "font.png")  # Replace 'your_image_file.png' with your PNG image path

def main():
    global root 
    root = tk.Tk()
    
    # Disable window close button (X button) action
    root.protocol("WM_DELETE_WINDOW", on_close)

    # Maximize the window to full-screen
    root.attributes('-fullscreen', True)

    # Bind Ctrl+K event to close the application
    root.bind('<Control-k>', on_ctrl_k)

    root.title("Four Zone Interface")

    # Set initial background image
    set_resized_background(root, "font.png")  # Replace 'your_image_file.png' with your PNG image path


    '''# Create the four zones
    zone1 = create_zone(root, 0, 0, 1, 1)
    zone2 = create_zone(root, 0, 1, 1, 1)
    zone3 = create_zone(root, 1, 0, 1, 1)
    zone4 = create_zone(root, 1, 1, 1, 1)

    # Add widgets to each zone
    add_widgets_to_zone(zone1, "Zone 1")
    add_widgets_to_zone(zone2, "Zone 2")
    add_widgets_to_zone(zone3, "Zone 3")
    add_widgets_to_zone(zone4, "Zone 4")'''

    # Configure grid weights to make zones expandable
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=6)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=4)

    root.bind("<Configure>", on_window_resize) 

    root.mainloop()

if __name__ == "__main__":
    main()






