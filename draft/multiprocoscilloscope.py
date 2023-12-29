import multiprocessing
import subprocess
from matplotlib import pyplot as plt 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

class myplot:
    def __init__(self, root):
        self.root = root
        self.root.title("Oscilloscope App")

        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.root)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.main()

    def subproc(self):
        proc = subprocess.Popen(
            ["python", r"C:\Repository\tkinter-Kiosk-interface\data_flow.py"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=False,  # Set this to True if 'python' is not in your PATH variable
            universal_newlines=True  # For text mode
        )
        return proc

    def plt_show(self, queue, stop_event):
        while not stop_event.is_set() or not queue.empty():
            self.figure.canvas.draw()
            self.figure.canvas.flush_events()

    def data_flow_acquisition(self, queue, stop_event):
        while not stop_event.is_set():
            proc = self.subproc()
            for line in iter(proc.stdout.readline, ''):
                    queue.put(line)

    def update_graph(self, queue, stop_event):
        while not stop_event.is_set() or not queue.empty():
            data = queue.get().strip()  # Assuming the data is a string
            # Process your data here and update the plot accordingly
            values = [int(val) for val in data.split(',')]
            x, y = values[0], values[1]
            print(x, y)
            self.ax.clear()
            self.ax.plot(x, y, 'b.')  # Plot as a single point
            self.ax.set_xlabel('X')
            self.ax.set_ylabel('Y')
            self.ax.set_title('Oscilloscope')
            
            

    def main(self):
        data_queue = multiprocessing.Queue()
        stop_event = multiprocessing.Event()
        
        acquisition_process = multiprocessing.Process(target=self.data_flow_acquisition, args=(data_queue, stop_event))
        plot_process = multiprocessing.Process(target=self.update_graph, args=(data_queue, stop_event))
        show_process = multiprocessing.Process(target=self.plt_show, args=(data_queue, stop_event))

        acquisition_process.start()
        plot_process.start()
        show_process.start()
        
        acquisition_process.join()
        plot_process.join()
        show_process.join()
        plt.show()

if __name__=='__main__':
    root = tk.Tk()
    myplot(root)