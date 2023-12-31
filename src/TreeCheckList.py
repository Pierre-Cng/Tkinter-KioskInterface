import tkinter as tk
from tkinter import ttk


class TreeCheckList(ttk.Treeview):
    def __init__(self, master, item_list=None, clicked_list=None, **kwargs):
        ttk.Treeview.__init__(self, master, **kwargs)
        self.unchecked = '\u2610'
        self.checked = '\u2612'
        self.separator = '.'
        self.bind('<<TreeviewSelect>>', self.item_ckeck)

    def item_check(self):
        pass 

    def insert_item(self):
        self.insert('', tk.END, values=values) 

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

    def add_item(self, item):
        """
        Add an item to the checklist. The item is the list of nodes separated
        by dots: `Item.SubItem.SubSubItem`. **This item is used as `iid`  at
        the underlying `Treeview` level.**
        """
        try:
            parent_iid, text = item.rsplit(self._separator, maxsplit=1)
        except ValueError:
            parent_iid, text = "", item
        self.insert(parent_iid, index='end', iid=item,
                    text=text+" "+self._unchecked, open=True)

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