import tkinter
import numpy as np
from matplotlib.backend_bases import key_press_handler
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure



class Content:
    def __init__(self, root):
        self.root = root
        self.figure()
        self.add_graph()
        self.add_toolbar()
        #self.toolbar.pack(side=tkinter.BOTTOM, fill=tkinter.X)
        self.canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True)
        self.root.attributes('-fullscreen', True)

    def figure(self):
        self.fig = Figure(figsize=(5, 4), dpi=100)
        t = np.arange(0, 3, .01)
        ax = self.fig.add_subplot()
        self.line, = ax.plot(t, 2 * np.sin(2 * np.pi * t))
        ax.set_xlabel("time [s]")
        ax.set_ylabel("f(t)")

    def add_graph(self):
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)  # A tk.DrawingArea.
        self.canvas.draw()
    
    def add_toolbar(self):
        # pack_toolbar=False will make it easier to use a layout manager later on.
        self.toolbar = NavigationToolbar2Tk(self.canvas, self.root, pack_toolbar=False)
        self.toolbar.update()

'''
canvas.mpl_connect(
    "key_press_event", lambda event: print(f"you pressed {event.key}"))
canvas.mpl_connect("key_press_event", key_press_handler)

button_quit = tkinter.Button(master=root, text="Quit", command=root.destroy)


    def update_frequency(new_val):
        f = float(new_val)
        y = 2 * np.sin(2 * np.pi * f * t)
        line.set_data(t, y)
        canvas.draw()


slider_update = tkinter.Scale(root, from_=1, to=5, orient=tkinter.HORIZONTAL,
                              command=update_frequency, label="Frequency [Hz]")

# Packing order is important. Widgets are processed sequentially and if there
# is no space left, because the window is too small, they are not displayed.
# The canvas is rather flexible in its size, so we pack it last which makes
# sure the UI controls are displayed as long as possible.
button_quit.pack(side=tkinter.BOTTOM)
slider_update.pack(side=tkinter.BOTTOM)



tkinter.mainloop()'''



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
        #self.plot_graph()

        # Button to trigger opening CSV and plotting
        #self.plot_button = tk.Button(self.frame, text="Open CSV and Plot", command=self.open_csv_and_plot)
        #self.plot_button.pack()

        self.open_csv_and_plot()
        #self.root.attributes('-fullscreen', True)
        #self.configure_kiosk_style()

    def set_frame(self):
        self.frame = tk.Frame(self.root)
        self.frame.grid(row=1, column=0, sticky="nw")

    def plot_graph(self):
        # Read CSV data and plot a graph
        data1 = pd.read_csv('output1.csv')  # Replace with your CSV file path
        data2 = pd.read_csv('output2.csv') 
        plt.figure(figsize=(6, 4))  # Adjust the figure size as needed
        plt.plot(data1['x'], data1['y'])  # Assuming 'x' and 'y' are column headers in your CSV
        plt.plot(data2['x'], data2['y'])
        plt.xlabel('X-axis Label')
        plt.ylabel('Y-axis Label')
        plt.title('Graph Title')
        plt.grid(True)

        # Embed the plot into Tkinter window
        canvas = FigureCanvasTkAgg(plt.gcf(), master=self.frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=False)
        #canvas.get_tk_widget().grid(row=0, column=0, sticky="nw")


    def open_csv_and_plot(self):
        # Function to open and plot CSV file data
        #file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])  # Open file dialog to select CSV file
        file_path = 'output1.csv' 
        if file_path:
            try:
                data = pd.read_csv(file_path)  # Read CSV file using Pandas
                fig = Figure( dpi=100)
                ax = fig.add_subplot()
                #fig, ax = plt.subplots()
                
                #plot default data:
                ax.plot(data)
                #df = pd.read_csv('name_of_file.csv', index_col=0)
                #data.plot()
                #plt.figure(figsize=(8, 6))  # Set the figure size
                #plt.plot(data)  # Plot the data from the CSV file
                #plt.xlabel('X-axis label')
                #plt.ylabel('Y-axis label')
                #plt.title('CSV Data Plot')
                '''
                self.fig = Figure(figsize=(5, 4), dpi=100)
                t = np.arange(0, 3, .01)
                ax = self.fig.add_subplot()
                self.line, = ax.plot(data)
                ax.set_xlabel("time [s]")
                ax.set_ylabel("f(t)")'''
                
                # Embedding the plot in tkinter window
                canvas = FigureCanvasTkAgg(fig, master=self.frame)
                canvas.draw()
                #canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
                canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
            except Exception as e:
                tk.messagebox.showerror("Error", f"Failed to load the file: {str(e)}")



    def configure_kiosk_style(self):
            # Disable window close button (X button) action
            self.root.protocol("WM_DELETE_WINDOW", self.on_close)
            # Maximize the window to full-screen
            self.root.attributes('-fullscreen', True)
            # Bind Ctrl+K event to close the application
            self.root.bind('<Control-k>', self.on_ctrl_k)

    def on_close(self):
            pass  # Handle the close event here

    def on_ctrl_k(self, event=None):
            # Close the interface when Ctrl+K is pressed
            self.root.quit()


            