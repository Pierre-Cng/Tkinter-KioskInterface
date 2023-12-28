import tkinter as tk
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Create the tkinter app window
root = tk.Tk()
root.attributes('-fullscreen', True)  # Set the window to full screen

# Function to open and plot CSV file data
def open_csv_and_plot():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])  # Open file dialog to select CSV file
    if file_path:
        try:
            data = pd.read_csv(file_path)  # Read CSV file using Pandas
            plt.figure(figsize=(8, 6))  # Set the figure size
            plt.plot(data)  # Plot the data from the CSV file
            plt.xlabel('X-axis label')
            plt.ylabel('Y-axis label')
            plt.title('CSV Data Plot')
            
            # Embedding the plot in tkinter window
            canvas = FigureCanvasTkAgg(plt.gcf(), master=root)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        except Exception as e:
            tk.messagebox.showerror("Error", f"Failed to load the file: {str(e)}")

# Button to trigger opening CSV and plotting
plot_button = tk.Button(root, text="Open CSV and Plot", command=open_csv_and_plot)
plot_button.pack()

# Function to exit the application
def close_app():
    root.destroy()

# Button to close the application
exit_button = tk.Button(root, text="Exit", command=close_app)
exit_button.pack()

root.mainloop()  # Start the tkinter event loop
