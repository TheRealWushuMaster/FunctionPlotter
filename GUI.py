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
        super().__init__(master=parent)
        
        # Create control widgets
        #frame_function = self.frame()
        function_label = self.label("Function: y = ")
        function_entry = self.text_input(text_var=function_text, width=50)
        
        # Place widgets
        #function_label.pack(side=tk.LEFT, padx=0, pady=DEF_PAD)
        #function_entry.pack(side=tk.LEFT, padx=0, pady=DEF_PAD)
        self.create_function_text()
        
        self.place(x=0, y=0, relwidth=1, height=100)

    def create_function_text(self):
        #frame = self.frame()
        #ttk.Label(text="Test").pack()
        function_label = self.label("Function: y = ")
        function_entry = self.text_input(function_text, width=FUNCTION_ENTRY_WIDTH)
        function_label.pack()
        function_entry.pack()

    def frame(self):
        frame = ttk.Frame(master=self)
        return frame
    
    def text_input(self, text_var = None, width=20):
        text_input = ttk.Entry(self, textvariable=text_var, width=width)
        return text_input
    
    def label(self, text):
        label = ttk.Label(self, text=text)
        return label

App()