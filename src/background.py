import tkinter as tk
from PIL import Image, ImageTk
import dummy
import time

def set_background(root, image_path):
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
    label.lower()

def loading_icon(root, process_status=True):
    # Center icon label
    icon_label = tk.Label(root, text="Icon", font=("Arial", 20))
    icon_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    return icon_label

def delete_icon(icon_label):
    time.sleep(3)
    icon_label.destroy()
    '''
    # Simulate process completion
    process_status = dummy.simulate_process()

    if process_status:
        # Hide the icon after the process is complete
        icon_label.after(0, icon_label.pack_forget())  # Schedule icon hide after a very short delay
    '''
