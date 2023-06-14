import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from settings import *
from define_vars import *

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
        
        # Create control widgets
        frame_function = self.frame()
        function_label = self.label(frame_function, "Function: y = ")
        function_entry = self.text_input(parent=frame_function, text_var=function_text, width=50)
        
        # Place widgets
        function_label.pack(side=tk.LEFT, padx=10, pady=10)
        function_entry.pack(side=tk.LEFT, padx=10, pady=10)
        
        self.place(x=0, y=0, relwidth=1, height=100)
        
    def frame(parent):
        frame = ttk.Frame(parent)
        return frame
    
    def text_input(parent, text_var = None, width=20):
        text_input = ttk.Entry(parent, textvariable=text_var, width=width)
        return text_input
    
    def label(parent, text):
        label = ttk.Label(parent, text=text)
        return label

App()