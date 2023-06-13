import tkinter as tk
import define_vars
import create_widgets
import functions as func

# Create the main window
window = tk.Tk()
window.title("Math Function Plotter")
window.iconbitmap("Plot.ico")

# Create variables
define_vars.create_variables()

# Add widgets
create_widgets.create_widgets(window, func.verify_values)

# Start the main event loop
window.mainloop()