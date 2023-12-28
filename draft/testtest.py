import tkinter as tk
import time
from PIL import Image, ImageTk

def create_zone(parent, row, column, rowspan=1, columnspan=1):
    zone = tk.Frame(parent, bg="white", highlightbackground="black", highlightthickness=1)
    zone.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan, sticky="nsew")
    return zone

def add_widgets_to_zone(zone, label_text):
    label = tk.Label(zone, text=label_text, font=("Arial", 12), padx=10, pady=10)
    label.pack(expand=True)

def set_resized_background(root, image_path, event=None):
    if event:
        window_width = event.width
        window_height = event.height
    else:
        window_width = root.winfo_width()
        window_height = root.winfo_height()

    # Open and resize the image to fit the window
    image = Image.open(image_path)
    resized_image = image.resize((window_width, window_height))

    # Convert the resized image to PhotoImage
    photo = ImageTk.PhotoImage(resized_image)
    
    # Set the resized image as background
    if hasattr(root, "background_label"):
        root.background_label.destroy()

    background_label = tk.Label(root, image=photo)
    background_label.image = photo  # To prevent image garbage collection
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    root.background_label = background_label

def on_window_resize(event):
    set_resized_background(root, "font.png", event)  # Replace 'your_image_file.png' with your PNG image path

def simulate_process():
    # Simulated process delay (you can replace this with your actual process)
    time.sleep(3)  # Sleep for 3 seconds as an example
    return True  # Simulated completion status

def main():
    global root
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.title("Resizable Background Image")

    # Set initial background image
    set_resized_background(root, "font.png")  # Replace 'your_image_file.png' with your PNG image path

    # Create the four zones
    zone1 = create_zone(root, 0, 0, 1, 1)
    zone2 = create_zone(root, 0, 1, 2, 1)
    zone3 = create_zone(root, 1, 0, 1, 1)
    zone4 = create_zone(root, 1, 1, 1, 1)

    # Add widgets to each zone
    add_widgets_to_zone(zone1, "Zone 1")
    add_widgets_to_zone(zone2, "Zone 2")
    add_widgets_to_zone(zone3, "Zone 3")
    add_widgets_to_zone(zone4, "Zone 4")

    # Center icon label
    icon_label = tk.Label(root, text="Icon", font=("Arial", 20))
    icon_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    icon_label.lift()  # Raise the icon label above other widgets

    # Simulate process completion
    process_status = simulate_process()

    if process_status:
        # Hide the icon after the process is complete
        icon_label.after(0, icon_label.place_forget())  # Schedule icon hide after a very short delay

    # Configure grid weights to make zones expandable
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)

    # Bind window resize event to handle background resizing
    root.bind("<Configure>", on_window_resize)

    root.mainloop()

if __name__ == "__main__":
    main()
