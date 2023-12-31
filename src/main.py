import tkinter as tk
from App import App
import tkinter.tix as Tix 

def main():
    
    root = tk.Tk()
    App(root)
    root.mainloop()
    '''
    root = Tix.Tk()
    App(root)
    root.update()
    root.mainloop()
    '''


if __name__ == "__main__":
    main() 