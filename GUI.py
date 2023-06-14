import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from settings import *

class App(tk.Tk):
    def __init__(self):
        
        # Setup
        super().__init__()
        self.title("Math Function Plotter")
        self.geometry(f"{WINDOW_SIZE[0]}x{WINDOW_SIZE[1]}")
        self.resizable = (True, True)
        self.iconbitmap("Plot.ico")
        
        # Widgets
        self.controls = Controls(self)

        # Layout
        #self.columnconfigure
        
        # Run
        self.mainloop()

class Controls(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        ttk.Label(self, background='red').pack(expand=True, fill='both')
        self.place(x=0, y=0, relwidth=0.3, relheight=1)
        

App()