import tkinter as tk
from tkinter import TclError, ttk
def create_main_window():
    root = tk.Tk()
    root.title("tk")
    root.resizable(0,0)
    try:
        root.attributes('-toolwindow', True)
    except TclError:
        print('Not supported on your platform')
    root.columnconfigure(0, weight=4)
    root.columnconfigure(1, weight=1)
    root.mainloop()
if __name__ == "__main__":
    create_main_window()
