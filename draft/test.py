'''import tkinter as tk

def create_columns(frame):
    # Create 5 columns with equal weight to distribute evenly
    for i in range(5):
        frame.grid_columnconfigure(i, weight=1)

def main():
    root = tk.Tk()
    root.title("Full Width Frame with 5 Columns")

    # Create a frame that will occupy the entire width of the screen
    main_frame = tk.Frame(root)
    main_frame.pack(fill="both", expand=True)  # Fill entire space of root

    create_columns(main_frame)

    # Create widgets or add contents to the columns
    for i in range(5):
        label = tk.Label(main_frame, text=f"Column {i + 1}", borderwidth=1, relief="solid")
        label.grid(row=0, column=i, sticky="nsew")  # Expand widget in all directions

    root.mainloop()

if __name__ == "__main__":
    main()'''

'''import tkinter as tk

def create_columns(frame):
    for i in range(5):
        frame.grid_columnconfigure(i, weight=1)

def main():
    root = tk.Tk()
    root.title("Multiline Label in 5 Columns")

    main_frame = tk.Frame(root)
    main_frame.pack(fill="both", expand=True)

    create_columns(main_frame)

    text = "This is a multiline label.\nIt can display several lines of text.\nYou can add more lines as needed."

    for i in range(5):
        label = tk.Label(main_frame, text=text, borderwidth=1, relief="solid", wraplength=100, justify="left")
        label.grid(row=0, column=i, sticky="nsew")

    root.mainloop()

if __name__ == "__main__":
    main()'''

import tkinter as tk

root = tk.Tk()
root.title("Button Styles")

# Different styles for the button
button_flat = tk.Button(root, text="Flat", relief="flat", borderwidth=2, bg="lightgray", fg="black")
button_flat.pack()

button_raised = tk.Button(root, text="Raised", relief="raised", borderwidth=4, bg="lightblue", fg="black")
button_raised.pack()

button_sunken = tk.Button(root, text="Sunken", relief="sunken", borderwidth=6, bg="lightgreen", fg="black")
button_sunken.pack()

button_groove = tk.Button(root, text="Groove", relief="groove", borderwidth=8, bg="lightyellow", fg="black")
button_groove.pack()

button_ridge = tk.Button(root, text="Ridge", relief="ridge", borderwidth=10, bg="lightcoral", fg="black")
button_ridge.pack()

root.mainloop()


