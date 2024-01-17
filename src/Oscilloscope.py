import tkinter as tk
import subprocess
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from queue import Queue
import threading
from matplotlib.figure import Figure

class Oscilloscope:
    def __init__(self, root):
        self.signals= {}
        self.clicked_signals = [] # access that oscilloscope.clicked_signals and refresh it on Tree clicked from action class
        self.root = root
        self.set_subplot()
        self.set_canvas()
        self.running = False
        self.stop_event = threading.Event()

    def set_subplot(self):
        self.figure = Figure((8, self.root.winfo_screenheight()//150))
        self.figure.set_facecolor('black')
        self.ax = self.figure.add_subplot()
        self.ax.set_facecolor('black')  # Set plot background to black
        self.ax.tick_params(axis='x', colors='white')  # Set x-axis ticks to white color
        self.ax.tick_params(axis='y', colors='white')  # Set y-axis ticks to white color
        self.ax.spines['bottom'].set_color('white')  # Set x-axis color to white
        self.ax.spines['top'].set_color('white')
        self.ax.spines['left'].set_color('white')  # Set y-axis color to white
        self.ax.spines['right'].set_color('white')

    def set_canvas(self):
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.root)
        self.root.grid_columnconfigure(1, weight=1)
        self.canvas.get_tk_widget().grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        
    def switch_oscilloscope(self, data_queue=None):
        self.running = not self.running
        if self.running:
            self.stop_event.clear()
            self.acquisition_thread = threading.Thread(target=self.acquire_data, args=(data_queue, self.stop_event))
            self.acquisition_thread.daemon = True
            self.acquisition_thread.start()
            self.update_plot()
        elif not self.running:
            self.stop_event.set()

    def acquire_data(self, data_queue, stop_event): # use queue and transform signal into dictionnary, append signals only from given clicked list
        while not stop_event.is_set():
            data = data_queue.get()
            signal, x, y = data.strip().split(',')
            if signal not in self.signals:
                self.signals[signal] = {'name': signal, 'x':[], 'y':[]}
            self.signals[signal]['x'].append(float(x))
            self.signals[signal]['y'].append(float(y))

    def update_plot(self):
        if self.running:
            self.ax.clear()
            for signal in self.clicked_signals:
                self.ax.plot(self.signals[signal]['x'][-10:-1], self.signals[signal]['y'][-10:-1], label=signal)
            if self.clicked_signals != []:
                self.ax.legend(loc='upper right', labelcolor='linecolor')
            self.ax.set_xlabel('Time', color='white')
            self.ax.set_ylabel('Amplitude', color='white')
            self.ax.set_title('Oscilloscope', color='white')
            self.canvas.draw()
            self.root.after(100, self.update_plot)

def main():
    root = tk.Tk()
    oscilloscope_app = Oscilloscope(root)
    oscilloscope_app.switch_oscilloscope()
    root.mainloop()

if __name__ == "__main__":
    main()
