import tkinter as tk

function_text = None
variable_name = None
start_value = None
end_value = None
num_points = None

def create_variables():
    global function_text, variable_name, start_value, end_value, num_points
    function_text = tk.StringVar(value = "sin(2*x)/x")
    variable_name = tk.StringVar(value = "x")
    start_value = tk.IntVar(value = -5)
    end_value = tk.IntVar(value = 5)
    num_points = tk.IntVar(value = 10)
    return function_text.get(), variable_name.get(), start_value.get(), end_value.get(), num_points.get()