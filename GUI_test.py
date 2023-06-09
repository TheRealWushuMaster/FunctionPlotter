import tkinter as tk
#from define_vars import create_variables
#from create_widgets import create_widgets
import define_vars
import create_widgets
import functions as func

# Create the main window
window = tk.Tk()
window.title("Math Function Plotter")

# Create variables
define_vars.create_variables()

# Add widgets
create_widgets.create_widgets(window, func.plot_math_function)

# Start the main event loop
window.mainloop()