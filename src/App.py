import tkinter as tk
from PIL import Image, ImageTk
import os
from Menu import Menu
from Content import Content
from Actions import Actions

background_image_path = os.path.join(os.getcwd(), r'src\image\font.png')

class App:
    def __init__(self, root):
        self.root = root
        self.configure_kiosk_style()
        #self.set_background()

        self.Menu = Menu(self.root)
        self.Content = Content(self.root)
        self.Actions = Actions(self.root, self.Menu, self.Content)

    def on_close(self):
        pass  # Handle the close event here

    def on_ctrl_k(self, event=None):
        # Close the interface when Ctrl+K is pressed
        self.root.quit()

    def configure_kiosk_style(self):
        # Disable window close button (X button) action
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        # Maximize the window to full-screen
        self.root.attributes('-fullscreen', True)
        # Bind Ctrl+K event to close the application
        self.root.bind('<Control-k>', self.on_ctrl_k)
        

    def set_background(self):
        # Open and resize the image to fit the window
        image = Image.open(background_image_path)
        window_width = self.root.winfo_screenwidth()
        window_height = self.root.winfo_screenheight()
        resized_image = image.resize((window_width, window_height))
        # Convert the resized image to PhotoImage
        photo = ImageTk.PhotoImage(resized_image)
        # Set the resized image as background
        label = tk.Label(self.root, image=photo)
        label.image = photo  # To prevent image garbage collection
        label.place(x=0, y=0, relwidth=1, relheight=1)
        label.lower()
