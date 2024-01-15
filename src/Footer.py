import tkinter as tk 
from Menu import Menu 

class Footer(Menu):
    def __init__(self, root):
        self.root = root
        self.set_frame()
        self.set_font()
        self.add_spacer(column=0, weight=4)
        self.jira_button = self.add_button('Create a Jira Ticket', 'darkred', column=4)

    def set_frame(self):
        self.frame = tk.Frame(self.root)
        self.frame.configure(bg='#111333', padx=20, pady=20)
        self.frame.pack(side='bottom', fill='both', expand=False)
