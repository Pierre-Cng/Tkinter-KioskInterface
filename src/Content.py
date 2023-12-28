import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import pandas as pd
from tkinter import filedialog
from matplotlib.figure import Figure
import numpy as np 

class Content:
    def __init__(self, root):
        self.root = root
        self.set_frame()
        self.plot_graph() 

    def set_frame(self):
        self.frame = tk.Frame(self.root)
        self.frame.grid(row=1, column=0, sticky="nw")

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
        #canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
