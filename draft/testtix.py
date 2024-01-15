import tkinter as tk 
import tkinter.tix as Tix 

class View(object):
    def __init__(self, root):
        self.root = root
        self.set_frame()
        self.makeCheckList()

    def set_frame(self):
        self.frame = tk.Frame(self.root)
        self.frame.configure(padx=20, pady=10)
        self.frame.pack(fill="both", expand=False)

    def makeCheckList(self):
        self.cl = Tix.CheckList(self.frame, browsecmd=self.selectItem)
        #self.cl.pack()
        self.frame.grid_columnconfigure(0, weight=1)
        self.cl.grid(row=0, column=0, sticky="nsew", padx=30, pady=10)
        self.cl.hlist.add("CL1", text="checklist1")
        self.cl.hlist.add("CL1.Item1", text="subitem1")
        self.cl.hlist.add("CL2", text="checklist2")
        self.cl.hlist.add("CL2.Item1", text="subitem1")
        self.cl.setstatus("CL2", "on")
        self.cl.setstatus("CL2.Item1", "on")
        self.cl.setstatus("CL1", "off")
        self.cl.setstatus("CL1.Item1", "off")
        self.cl.autosetmode()

    def selectItem(self, item):
        print(item, self.cl.getstatus(item))

def main():
    root = Tix.Tk()
    view = View(root)
    root.update()
    root.mainloop()

if __name__ == '__main__':
    main()