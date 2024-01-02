import tkinter as tk 
from testclaa import TtkCheckList

items = [
    'Item',
    'Item.SubItem1',
    'Item.SubItem2',
    'Item.SubItem2.SubSubItem1',
    'Item.SubItem2.SubSubItem2',
    'Item.SubItem2.SubSubItem3',
    'Item.SubItem3',
    'Item.SubItem3.SubSubItem1',
    'Item.SubItem4'
]

root = tk.Tk()
root.title('Test')
root.geometry('400x300')

check_list = TtkCheckList(root, height=len(items))

for item in items:
    check_list.add_item(item)
check_list.pack()

root.mainloop()