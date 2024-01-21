import time 
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import threading
from matplotlib.figure import Figure

class Stopwatch:
    def __init__(self, root, font, row=0, column=0):
        self.add_stopwatch(root, font, row, column)

    def add_stopwatch(self, root, font, row=0, column=0):
        self.start_time = None
        self.stopwatch_running = False
        self.time_label = tk.Label(root, text="00:00:00", borderwidth=1, relief="solid", font=font)
        root.grid_columnconfigure(column, weight=2)
        self.time_label.grid(row=row, column=column, sticky="nsew", padx=10, pady=10)

    def start_stopwatch(self):
        if self.start_time is not None:
            self.reset_stopwatch()
        self.stopwatch_running = True
        self.start_time = time.time() 
        self.update_time()

    def stop_stopwatch(self):
        self.stopwatch_running = False

    def update_time(self):
        if self.stopwatch_running:
            elapsed_time = time.time() - self.start_time
            hours = int(elapsed_time // 3600)
            minutes = int((elapsed_time % 3600) // 60)
            seconds = int(elapsed_time % 60)
            time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            self.time_label.config(text=time_str)
        self.time_label.after(1000, self.update_time)

    def reset_stopwatch(self):
        self.time_label.config(text="00:00:00")

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
                if len(self.signals[signal]['x'])>100:
                    self.ax.plot(self.signals[signal]['x'][-100:-1], self.signals[signal]['y'][-100:-1], label=signal)
                else:
                    self.ax.plot(self.signals[signal]['x'], self.signals[signal]['y'], label=signal)
            if self.clicked_signals != []:
                self.ax.legend(loc='upper right', labelcolor='linecolor')
            self.ax.set_xlabel('Time', color='white')
            self.ax.set_ylabel('Amplitude', color='white')
            self.ax.set_title('Oscilloscope', color='white')
            self.canvas.draw()
            self.root.after(100, self.update_plot)

class TreeCheckList(ttk.Treeview):
    def __init__(self, master, item_dict=None, clicked_list=[], **kwargs):
        self.clicked_list = clicked_list
        columns = ('Status')
        ttk.Treeview.__init__(self, master, columns=columns, show='tree', **kwargs)
        self.unchecked = '\u2610'
        self.checked = '\u2611'
        if item_dict is not None:
            self.add_items(item_dict)

    def switch_bool_box(self, value):
        dict = {self.checked:True, self.unchecked:False}
        reverse_dict= {v: k for k, v in dict.items()}
        if value in dict:
            return dict[value]
        if value in reverse_dict:
            return reverse_dict[value]

    def add_items(self, item_dict):
        for channel in item_dict:
            self.insert('', tk.END, iid=channel, text='Channel: ' + channel, open=False, tags=channel)
            for message in item_dict[channel].keys():
                iid_msg = channel + '.' + message
                self.insert(channel, tk.END, iid=iid_msg, text='\u2937 Message: ' + message, open=True, tags=iid_msg)
                for signal in item_dict[channel][message]:
                    iid_sig = iid_msg + '.' + signal
                    checked = iid_sig in self.clicked_list
                    self.insert(iid_msg, tk.END, iid=iid_sig, text='\u25b9 Signal: ' + signal, values=self.switch_bool_box(checked), open=True, tags=iid_sig) 

    def check_item(self, event):
        for selected_item in self.selection():
            if isinstance(self.item(selected_item)['values'], list):
                status = self.item(selected_item)['values'][0]
                text = self.item(selected_item)['text']
                iid = self.item(selected_item)['tags'][0]
                if 'Signal:' in text: 
                    status = status != self.checked
                    if status:
                        self.clicked_list.append(iid)
                    elif iid in self.clicked_list:
                        self.clicked_list.remove(iid)
                self.item(selected_item, values=self.switch_bool_box(status))
