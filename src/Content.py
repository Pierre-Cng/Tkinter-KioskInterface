import tkinter as tk
from Oscilloscope import Oscilloscope
from TreeCheckList import TreeCheckList

class Content:
    def __init__(self, root):
        self.root = root
        self.set_frame()
        self.set_tree()
        self.graph = Oscilloscope(self.frame)
    
    def set_frame(self):
        self.frame = tk.Frame(self.root)
        self.frame.configure(padx=20, pady=50)
        self.frame.pack(fill="both", expand=False)

    def set_tree(self):
        items = {'Channel1': {'Message1': ['signal1', 'signal2']}}
        self.tree = TreeCheckList(self.frame, item_dict=items, height=len(items))
        self.frame.grid_columnconfigure(0, weight=1)
        self.tree.grid(row=0, column=0, sticky="nsew", padx=30, pady=10)
