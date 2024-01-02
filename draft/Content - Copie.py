import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import pandas as pd
from tkinter import filedialog
from matplotlib.figure import Figure
import numpy as np 
from tkinter import IntVar

class Content:
    def __init__(self, root):
        self.root = root
        self.set_frame()
        self.add_option_frame()
        self.plot_graph() 

    def set_frame(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack(fill="y", expand=True)

        #self.frame.grid_columnconfigure(column, weight=2)
        #label.grid(row=row, column=column, sticky="nsew", padx=10, pady=10)


    def add_option_frame(self):
        # Checkable options for the graph placed on the left
        options_frame = tk.Frame(self.frame)
        self.frame.grid_columnconfigure(0, weight=1)
        options_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        
      

        check_var1 = IntVar()
        check_var2 = IntVar()
        check_var3 = IntVar()

        check1 = tk.Checkbutton(options_frame, text="Option 1", variable=check_var1)
        check1.pack(anchor=tk.W)

        check2 = tk.Checkbutton(options_frame, text="Option 2", variable=check_var2)
        check2.pack(anchor=tk.W)

        check3 = tk.Checkbutton(options_frame, text="Option 3", variable=check_var3)
        check3.pack(anchor=tk.W)

    def plot_graph(self):
        # Read CSV data and plot a graph
        data1 = pd.read_csv('output1.csv')  # Replace with your CSV file path
        data2 = pd.read_csv('output2.csv') 

        fig = Figure( dpi=100)

        ax1 = fig.add_subplot()
        ax2 = fig.add_subplot()

        ax1.plot(data1)
        ax2.plot(data2)
        
        # Embedding the plot in tkinter window
        canvas = FigureCanvasTkAgg(fig, master=self.frame)
        canvas.draw()
        #canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.frame.grid_columnconfigure(1, weight=1)
        canvas.get_tk_widget().grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

                