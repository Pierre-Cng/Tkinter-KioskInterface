import tkinter as tk
import subprocess
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from queue import Queue
from threading import Thread

class Oscilloscope:
    def __init__(self, root):
        self.data = []
        self.root = root
       

        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.root)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.running = False
        self.data_queue = Queue()
        self.start_button = tk.Button(self.root, text="Start", command=self.start_oscilloscope)
        self.start_button.pack()
        

    def start_oscilloscope(self):
        self.running = not self.running
        if self.running:
            self.start_button.config(text="Stop")
            self.acquisition_thread = Thread(target=self.acquire_data)
            self.acquisition_thread.daemon = True
            self.acquisition_thread.start()
            self.update_plot()
        else:
            self.start_button.config(text="Start")

    def acquire_data(self):
        # Start the subprocess running the Python script (replace paths as needed)
        self.proc = subprocess.Popen(
            ["python", r"C:\Repository\tkinter-Kiosk-interface\data_flow.py"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=False,  # Set this to True if 'python' is not in your PATH variable
            universal_newlines=True  # For text mode
        )

        for line in iter(self.proc.stdout.readline, ''):
            line = line.strip()
            x, y = line.split(',')
            self.data.append((int(x), int(y)))
        self.proc.stdout.close()

    def update_plot(self):
        if self.running:
            self.ax.clear()
            if self.data:
                x, y = zip(*self.data)
                self.ax.plot(x, y, 'b-')
            self.ax.set_xlabel('Time')
            self.ax.set_ylabel('Amplitude')
            self.ax.set_title('Oscilloscope')
            self.canvas.draw()

            self.root.after(100, self.update_plot)

def main():
    root = tk.Tk()
    oscilloscope_app = Oscilloscope(root)
    root.mainloop()

if __name__ == "__main__":
    main()
