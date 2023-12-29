import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import threading
import time

class OscilloscopeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Oscilloscope App")

        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.root)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.running = False
        self.data = []

        self.start_button = tk.Button(self.root, text="Start", command=self.start_oscilloscope)
        self.start_button.pack()

    def start_oscilloscope(self):
        self.running = not self.running
        if self.running:
            self.start_button.config(text="Stop")
            self.acquisition_thread = threading.Thread(target=self.acquire_data)
            self.acquisition_thread.daemon = True
            self.acquisition_thread.start()
            self.update_plot()
        else:
            self.start_button.config(text="Start")

    def acquire_data(self):
        x = 0
        y = 100
        while self.running:
            x += 1
            y -= 1
            self.data.append((x, y))
            time.sleep(0.1)  # Simulating data acquisition delay

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
    oscilloscope_app = OscilloscopeApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
