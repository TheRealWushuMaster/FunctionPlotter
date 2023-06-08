import tkinter as tk
from create_widgets import create_widgets
import functions as func
import define_vars as def_vars
#from functions import plot_math_function

# Create the main window
window = tk.Tk()
window.title("Math Function Plotter")

# Add your widgets here
create_widgets(window, func.plot_math_function, def_vars.function_text)

# Start the main event loop
window.mainloop()
