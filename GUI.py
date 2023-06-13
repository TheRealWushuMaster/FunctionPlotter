import customtkinter as ctk
from settings import *

class GUI(ctk.CTk):
    def __init__(self):
        
        # Setup
        super().__init__()
        self.title("Math Function Plotter")
        self.geometry(f"{WINDOW_SIZE[0]}x{WINDOW_SIZE[1]}")
        
        # Layout
        self.columnconfigure
        
        # Run
        self.mainloop()

GUI()