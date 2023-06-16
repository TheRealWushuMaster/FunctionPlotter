import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from settings import *
import define_vars

class App(tk.Tk):
    def __init__(self):
        
        # Setup
        super().__init__()
        self.title("Math Function Plotter")
        self.geometry(f"{WINDOW_SIZE[0]}x{WINDOW_SIZE[1]}")
        self.resizable = (True, True)
        self.iconbitmap("Plot.ico")
        define_vars.create_variables()

        # Widgets
        Controls(self)

        # Run
        self.mainloop()

class Controls(ttk.Frame):
    def __init__(self, parent):
        super().__init__(master=parent)
        
        # Create control widgets
        function_frame = self.create_function_frame()
        variable_limits_frame = self.create_variable_limits_frame()
        points_per_unit_frame = self.create_points_per_unit_frame()
        
        # Place widgets
        function_frame.pack(padx=DEF_PAD, pady=DEF_PAD)
        variable_limits_frame.pack(padx=DEF_PAD, pady=0)
        points_per_unit_frame.pack(padx=DEF_PAD, pady=DEF_PAD)
        
        canvas = tk.Canvas(parent, bg="white")
        self.pack()
        #self.place(x=0, y=0, relwidth=1, height=130)
        canvas.pack(expand=True, fill="both")

    def create_function_frame(self):
        function_text_frame = ttk.Frame(master=self)
        ttk.Label(master=function_text_frame, text="Function: y =").pack(side=tk.LEFT)
        ttk.Entry(master=function_text_frame, textvariable=define_vars.function_text, width=FUNCTION_ENTRY_WIDTH).pack(side=tk.LEFT)
        return function_text_frame
    
    def create_variable_limits_frame(self):
        variable_limits_frame = ttk.Frame(master=self)
        ttk.Label(master=variable_limits_frame, text=f"Limits of the {define_vars.variable_name.get()} variable").pack(pady=int(DEF_PAD/2))
        ttk.Label(master=variable_limits_frame, text="Start:").pack(side=tk.LEFT)
        ttk.Entry(master=variable_limits_frame, textvariable=define_vars.start_value, width=DEFAULT_ENTRY_WIDTH).pack(side=tk.LEFT)
        ttk.Label(master=variable_limits_frame, text="End:").pack(side=tk.LEFT)
        ttk.Entry(master=variable_limits_frame, textvariable=define_vars.end_value, width=DEFAULT_ENTRY_WIDTH).pack(side=tk.LEFT)
        return variable_limits_frame
    
    def create_points_per_unit_frame(self):
        points_per_unit_frame = ttk.Frame(master=self)
        ttk.Label(master=points_per_unit_frame, text="Points per unit:").pack(side=tk.LEFT)
        ttk.Entry(master=points_per_unit_frame, textvariable=define_vars.num_points, width=DEFAULT_ENTRY_WIDTH).pack(side=tk.LEFT)
        return points_per_unit_frame

App()