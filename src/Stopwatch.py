import time 
import tkinter as tk

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
