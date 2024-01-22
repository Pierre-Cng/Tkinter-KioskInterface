import tkinter as tk 
from queue import Queue
import threading 
import math 
from ComManager import Configurator, RequestThreader
import time 
import cantools 
from tkinter import messagebox

class Actions:
    def __init__(self, root, menu, content, footer, popup):
        self.connection_verified = False
        self.root = root 
        self.menu = menu 
        self.content = content 
        self.footer = footer
        self.popup = popup
        self.configurator = Configurator()
        self.configure_combos()
        self.configure_buttons()
        self.configure_label()
        self.configure_tree()
        self.stop_event = threading.Event()
        self.message_queue = Queue()
        self.requestthreader = RequestThreader()

    def configure_combos(self):
        self.combo_choices = {}
        self.menu.combos['category'].config(values=self.configurator.data['Combos']['Category'])
        self.menu.combos['number'].config(values=self.configurator.data['Combos']['Number'])
        self.menu.combos['category'].current(0)
        self.menu.combos['number'].current(0)
        self.menu.combos['category'].bind('<<ComboboxSelected>>', lambda event, arg='category': self.on_combo_change(event, arg))
        self.menu.combos['number'].bind('<<ComboboxSelected>>', lambda event, arg='number': self.on_combo_change(event, arg))

    def configure_buttons(self):
        self.menu.verify_button.config(command=self.verify_config)
        self.menu.config_button.config(command=self.modify_config)
        self.menu.recording_button.config(command=self.start_recording)
        self.menu.send_button.config(command=self.send_data)

    def configure_label(self):
        self.label_text = tk.StringVar()
        initial_text = ''
        for key, value in self.configurator.data['Devices'].items():
            initial_text += f'{key} - disconneted - {value}\n'
        self.label_text.set(initial_text)
        self.label_text.trace_add('write', self.on_label_change)
        self.menu.config_label.config(textvariable=self.label_text)
    
    def tree_items(self):
        items = {}
        for key, value in self.configurator.data['Devices'].items():
            items[key] = {}
            dbc = cantools.database.load_file(value)
            for message in dbc.messages:
                items[key][message.name] = []
                for signal in message.signals:
                    items[key][message.name].append(signal.name)
        return items
    
    def configure_tree(self):
        items = self.tree_items()
        self.content.tree.add_items(items)
        self.content.tree.bind('<<TreeviewSelect>>', self.on_tree_change)

    def on_combo_change(self, event, comboID):
        self.combo_choices[comboID] = self.menu.combos[comboID].get()

    def on_label_change(self, *args):
        if self.label_text.get() == 'Loading...':
            print('identify request')
            self.requestthreader.thread_identify_request(self.configurator.data['Devices'], self.label_text)

    def on_tree_change(self, event):
        self.content.tree.check_item(event)
        self.content.graph.clicked_signals = self.content.tree.clicked_list

    def verify_config(self):
        self.label_text.set('Loading...')
        self.connection_verified = True

    def modify_config(self):
        self.popup.activate()
        # open pop up with list of available stack and available dbc - allow user to associate them together 
        # option to refresh dbc and stack and fetch latest 
        # update config label 

    def dummy_thread_func(self, data_queue, stop_event):
        data = 0 
        while not stop_event.is_set():
            data += 1 
            data_queue.put(f'Channel1.Message1.signal1, {data}, {math.sin(data)}')
            data_queue.put(f'Channel1.Message1.signal2, {data}, {math.cos(data)}')
        
    def start_recording(self):
        # Verify if combos and config have been set
        if len(self.combo_choices)<1:
            messagebox.showinfo("Warning", "Please select a vehicle category and number.")
            return
        if not self.connection_verified:
            messagebox.showinfo("Warning", "Please verify the config before recording.")
            return
        # Stopwatch
        self.menu.stopwatch.start_stopwatch()
        # Start command 
        self.stop_event.clear()
        self.requestthreader.thread_start_request(self.message_queue, self.stop_event)
        '''
        self.dummy_thread = threading.Thread(target=self.dummy_thread_func, args=(self.data_queue, self.stop_event))
        self.dummy_thread.daemon = True
        self.dummy_thread.start()
        '''
        self.content.graph.switch_oscilloscope(self.message_queue)
        self.menu.recording_button.config(text="Stop Recording", command=self.stop_recording, bg='red')
        #print(self.content.tree.clicked_list)'''

    def stop_recording(self):
        # lauch script to save logs and stop stack - stop stopwatch - stop oscilloscope - allow send data button  
        self.stop_event.set()
        self.menu.stopwatch.stop_stopwatch()
        self.content.graph.switch_oscilloscope()
        self.requestthreader.thread_stop_request()
        #with open('dictdump.json', 'w') as json_file:
        #    json.dump(self.content.graph.signals, json_file, indent=4)
        self.menu.recording_button.config(text="Start Recording", command=self.start_recording, bg='green')
        
    def send_data(self):
        pass
    # when allowed send recorded logs under vehicule + number file name to s3 server 
