import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import pandas as pd
from tkinter import filedialog

import numpy as np 
from tkinter import IntVar
from Oscilloscope import Oscilloscope
from tkinter import ttk
import tkinter.tix as Tix 
from TreeCheckList import TreeCheckList

class Content:
    def __init__(self, root):
        self.root = root
        self.set_frame()
        #self.graph_menu()
        #self.makeCheckList()
        self.widget()
        self.graph = Oscilloscope(self.frame)
    
    def set_frame(self):
        self.frame = Tix.Frame(self.root)
        self.frame.configure(padx=20, pady=10)
        self.frame.pack(fill="both", expand=False)
    '''
    def graph_menu(self):
        # Checkable options for the graph placed on the left
        options_frame = tk.Frame(self.frame)
        self.frame.grid_columnconfigure(0, weight=1)
        options_frame.grid(row=0, column=0, sticky="nsew", padx=30, pady=10)
        
        check_var1 = IntVar()
        check_var2 = IntVar()
        check_var3 = IntVar()

        check1 = tk.Checkbutton(options_frame, text="Option 1", variable=check_var1)
        check1.pack(anchor=tk.W)

        check2 = tk.Checkbutton(options_frame, text="Option 2", variable=check_var2)
        check2.pack(anchor=tk.W)

        check3 = tk.Checkbutton(options_frame, text="Option 3", variable=check_var3)
        check3.pack(anchor=tk.W)
    '''

    '''
    def graph_menu(self):
        options_frame = ttk.Treeview(self.frame, columns=('Checkboxes',), show='tree')
        options_frame.heading('#0', text='Tree Elements')

        num_trees = 4  # Number of trees
        num_checkboxes_per_tree = 5  # Number of checkboxes in each tree

        for tree_idx in range(num_trees):
            tree_node = options_frame.insert('', 'end', text=f'Tree {tree_idx + 1}')
            for checkbox_idx in range(num_checkboxes_per_tree):
                checkbox = tk.Checkbutton(self.frame, text=f'Checkbox {checkbox_idx + 1} of Tree {tree_idx + 1}')
                options_frame_window = options_frame.insert(tree_node, 'end', text='', window=checkbox)
                options_frame.item(options_frame_window, open=True)

    
          for tree_idx in range(num_trees):
            tree_node = options_frame.insert('', 'end', text=f'Tree {tree_idx + 1}')
            for checkbox_idx in range(num_checkboxes_per_tree):
                checkbox_label = f'Checkbox {checkbox_idx + 1} of Tree {tree_idx + 1}'
                options_frame.insert(tree_node, 'end', text=checkbox_label)

        #options_frame.pack(expand=True, fill=tk.BOTH)
        self.frame.grid_columnconfigure(0, weight=1)
        options_frame.grid(row=0, column=0, sticky="nsew", padx=30, pady=10)

    '''
    '''
    def graph_menu(self):
        check_list = Tix.CheckList(self.frame, browsecmd=self.on_select)
        self.frame.grid_columnconfigure(0, weight=1)
        check_list.grid(row=0, column=0, sticky="nsew", padx=30, pady=10)
        #check_list.pack(expand=tk.YES, fill=tk.BOTH)

        num_trees = 4  # Number of trees
        num_checkboxes_per_tree = 5  # Number of checkboxes in each tree

        for tree_idx in range(num_trees):
            tree_id = check_list.insert('', 'end', text=f'Tree {tree_idx + 1}')
            for checkbox_idx in range(num_checkboxes_per_tree):
                checkbox_text = f'Checkbox {checkbox_idx + 1} of Tree {tree_idx + 1}'
                check_list.insert(tree_id, 'end', text=checkbox_text)

    def on_select(self, item):
        print(f"Selected item: {item}")
    '''
    '''
    def makeCheckList(self):
        self.cl = Tix.CheckList(self.frame, browsecmd=self.selectItem)
        #self.cl.pack()
        self.frame.grid_columnconfigure(0, weight=1)
        self.cl.grid(row=0, column=0, sticky="nsew", padx=30, pady=10)
        self.cl.hlist.add("CL1", text="checklist1")
        self.cl.hlist.add("CL1.Item1", text="subitem1")
        self.cl.hlist.add("CL2", text="checklist2")
        self.cl.hlist.add("CL2.Item1", text="subitem1")
        self.cl.setstatus("CL2", "on")
        self.cl.setstatus("CL2.Item1", "on")
        self.cl.setstatus("CL1", "off")
        self.cl.setstatus("CL1.Item1", "off")
        self.cl.autosetmode()

    def selectItem(self, item):
        print(item, self.cl.getstatus(item))

    '''
    def widget(self):
        items = [
            'Channel1',
            'Channel1.Device1',
            'Channel1.Device1.Signal1',
            'Channel1.Device1.Signal2',
            'Channel1.Device1.Signal3',
            'Channel1.Device2',
            'Channel1.Device2.Signal1',
            'Channel1.Device2.Signal2',
            'Channel1.Device2.Signal3',
            'Channel2',
            'Channel2.Device1',
            'Channel2.Device1.Signal1',
            'Channel2.Device1.Signal2',
            'Channel2.Device1.Signal3',
            'Channel2.Device2',
            'Channel2.Device2.Signal1',
            'Channel2.Device2.Signal2',
            'Channel2.Device2.Signal3',
        ]
        check_list = TreeCheckList(self.frame, item_list=items, height=len(items))
        self.frame.grid_columnconfigure(0, weight=1)
        check_list.grid(row=0, column=0, sticky="nsew", padx=30, pady=10)
