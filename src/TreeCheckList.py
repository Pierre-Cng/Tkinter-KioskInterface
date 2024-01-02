import tkinter as tk
from tkinter import ttk


class TreeCheckList(ttk.Treeview):
    def __init__(self, master, item_list=None, clicked_list=None, **kwargs):
        columns = ('status', 'iid')
        ttk.Treeview.__init__(self, master, columns=columns, show='tree', **kwargs)
        self.unchecked = '\u2610'
        self.checked = '\u2612'
        self.separator = '.'
        if item_list is not None:
            self.add_items(item_list, clicked_list)
        self.bind('<<TreeviewSelect>>', self.check_item)

    def switch_bool_box(self, value, iid=''):
        dict = {self.checked:True, self.unchecked:False, '':''}
        reverse_dict= {v: k for k, v in dict.items()}
        if value in dict:
            return iid, dict[value]
        if value in reverse_dict:
            return iid, reverse_dict[value]

    def add_items(self, item_list, clicked_list=None):
        clicked_list = ('Item')
        for item in item_list:
            try:
                parent, iid = item.rsplit(self.separator, maxsplit=1)
                if clicked_list is not None:
                    value = iid in clicked_list
                else:
                    value = False
            except ValueError:
                parent, iid, value = '', item, ''
            self.insert(parent, tk.END, iid=item, values=self.switch_bool_box(value, iid), open=True) 

    def check_item(self, event):
        for selected_item in self.selection():
            iid, value = self.item(selected_item)['values']
            if value != '': 
                value = value != self.checked 
            self.item(selected_item, values=(self.switch_bool_box(value, iid)))
           
'''
class TtkCheckList(ttk.Treeview):
    def __init__(self, master=None, width=200, clicked=None, separator='.',
                 unchecked=BALLOT_BOX, checked=BALLOT_BOX_WITH_X, **kwargs):
 
        self._clicked = self.toggle if clicked is None else clicked

        self.column('#0', width=width, stretch=tk.YES)
        self.bind("<Button-1>", self._item_click, True)

    def _item_click(self, event):
        assert event.widget == self
        x, y = event.x, event.y
        element = self.identify("element", x, y)
        if element == "text":
            iid = self.identify_row(y)
            self._clicked(iid)

    def toggle(self, iid):
        """
        Toggle the checkbox `iid`
        """
        text = self.item(iid, "text")
        checked = text[-1] == self._checked
        status = self._unchecked if checked else self._checked
        self.item(iid, text=text[:-1] + status)

    def checked(self, iid):
        """
        Return True if checkbox `iid` is checked
        """
        text = self.item(iid, "text")
        return text[-1] == self._checked

    def check(self, iid):
        """
        Check the checkbox `iid`
        """
        text = self.item(iid, "text")
        if text[-1] == self._unchecked:
            self.item(iid, text=text[:-1] + self._checked)

    def uncheck(self, iid):
        """
        Uncheck the checkbox `iid`
        """
        text = self.item(iid, "text")
        if text[-1] == self._checked:
            self.item(iid, text=text[:-1] + self._unchecked)


    # json function - is checked - status - colum for the box 
'''