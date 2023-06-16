import tkinter as tk
from tkinter import ttk
from settings import *
import define_vars
import functions
import webbrowser

class App(tk.Tk):
    def __init__(self):
        
        # Setup
        super().__init__()
        self.title("Math Function Plotter")
        self.geometry(f"{WINDOW_SIZE[0]}x{WINDOW_SIZE[1]}")
        self.resizable = (True, True)
        self.minsize(MINIMUM_SIZE[0], MINIMUM_SIZE[1])
        self.iconbitmap("Plot.ico")
        define_vars.create_variables()
        self.configure(background=DEFAULT_BACKGROUND)

        # Widgets
        Controls(self)
        GitHubLink = ttk.Label(master=self, text="GitHub page", background=DEFAULT_BACKGROUND, foreground="red", cursor="hand2")
        GitHubLink.bind("<Button-1>", lambda e: webbrowser.open_new("https://github.com/TheRealWushuMaster/FunctionPlotter"))
        GitHubLink.place(x=0, y=155)

        # Run
        self.mainloop()

class Controls(tk.Frame):
    def __init__(self, parent):
        super().__init__(master=parent)
        
        # Set background color
        self.configure(background=DEFAULT_BACKGROUND)
        
        # Create control widgets
        function_frame = self.create_function_frame()
        variable_limits_frame = self.create_variable_limits_frame()
        points_per_unit_frame = self.create_points_per_unit_frame()
        
        # Place widgets
        function_frame.pack(padx=DEF_PAD, pady=DEF_PAD)
        variable_limits_frame.pack(padx=DEF_PAD, pady=0)
        points_per_unit_frame.pack(padx=DEF_PAD, pady=DEF_PAD)
        
        # Add the canvas and plot button
        canvas = tk.Canvas(parent, bg="white")
        self.pack()
        tk.Button(master=self, text="Plot", command=lambda: functions.verify_values(canvas), width=15).pack(pady=DEF_PAD)
        canvas.pack(expand=True, fill="both")

    def create_function_frame(self):
        function_text_frame = tk.Frame(master=self, background=DEFAULT_BACKGROUND)
        ttk.Label(master=function_text_frame, text="Function: y =", background=DEFAULT_BACKGROUND, foreground=DEFAULT_LABEL_TEXT_COLOR).pack(side=tk.LEFT)
        ttk.Entry(master=function_text_frame, textvariable=define_vars.function_text, width=FUNCTION_ENTRY_WIDTH, background=DEFAULT_BACKGROUND).pack(side=tk.LEFT)
        return function_text_frame
    
    def create_variable_limits_frame(self):
        variable_limits_frame = tk.Frame(master=self, background=DEFAULT_BACKGROUND)
        ttk.Label(master=variable_limits_frame, text=f"Limits of the {define_vars.variable_name.get()} variable", background=DEFAULT_BACKGROUND, foreground=DEFAULT_LABEL_TEXT_COLOR).pack(pady=int(DEF_PAD/2))
        ttk.Label(master=variable_limits_frame, text="Start:", background=DEFAULT_BACKGROUND, foreground=DEFAULT_LABEL_TEXT_COLOR).pack(side=tk.LEFT)
        ttk.Entry(master=variable_limits_frame, textvariable=define_vars.start_value, width=DEFAULT_ENTRY_WIDTH, background=DEFAULT_BACKGROUND).pack(side=tk.LEFT)
        ttk.Label(master=variable_limits_frame, text="End:", background=DEFAULT_BACKGROUND, foreground=DEFAULT_LABEL_TEXT_COLOR).pack(side=tk.LEFT)
        ttk.Entry(master=variable_limits_frame, textvariable=define_vars.end_value, width=DEFAULT_ENTRY_WIDTH, background=DEFAULT_BACKGROUND).pack(side=tk.LEFT)
        return variable_limits_frame
    
    def create_points_per_unit_frame(self):
        points_per_unit_frame = tk.Frame(master=self, background=DEFAULT_BACKGROUND)
        ttk.Label(master=points_per_unit_frame, text="Points per unit:", background=DEFAULT_BACKGROUND, foreground=DEFAULT_LABEL_TEXT_COLOR).pack(side=tk.LEFT)
        ttk.Entry(master=points_per_unit_frame, textvariable=define_vars.num_points, width=DEFAULT_ENTRY_WIDTH, background=DEFAULT_BACKGROUND).pack(side=tk.LEFT)
        return points_per_unit_frame

App()