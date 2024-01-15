import tkinter as tk
from tkinter import ttk

class TreeCheckList(ttk.Treeview):
    def __init__(self, master, item_dict=None, clicked_list=[], **kwargs):
        self.clicked_list = clicked_list
        columns = ('Status')
        ttk.Treeview.__init__(self, master, columns=columns, show='tree', **kwargs)
        self.unchecked = '\u2610'
        self.checked = '\u2611'
        if item_dict is not None:
            self.add_items(item_dict)
        self.bind('<<TreeviewSelect>>', self.check_item)

    def switch_bool_box(self, value):
        dict = {self.checked:True, self.unchecked:False}
        reverse_dict= {v: k for k, v in dict.items()}
        if value in dict:
            return dict[value]
        if value in reverse_dict:
            return reverse_dict[value]

    def add_items(self, item_dict):
        for channel in item_dict:
            self.insert('', tk.END, iid=channel, text='Channel: ' + channel, open=True, tags=channel)
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
