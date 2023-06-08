import tkinter as tk
from create_widgets import create_widgets
import functions as func
from define_vars import function_text, variable_name, start_value, end_value, num_points
#from functions import plot_math_function

# Create the main window
window = tk.Tk()
window.title("Math Function Plotter")

# Add your widgets here
create_widgets(window, func.plot_math_function, function_text)

# Start the main event loop
window.mainloop()
