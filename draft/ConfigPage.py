import tkinter as tk

class ConfigPage:
    def __init__(self, root):
        self.root = root 

    def create_popup():
        popup = tk.Toplevel(self.root)
        popup.title("Popup Window")
        popup.geometry("200x100")
        label = tk.Label(popup, text="This is a popup window")
        label.pack(padx=20, pady=20)



