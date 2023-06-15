import tkinter as tk
from settings import *

function_text = None
variable_name = None
start_value = None
end_value = None
num_points = None

def create_variables():
    global function_text, variable_name, start_value, end_value, num_points
    function_text = tk.StringVar(value = DEF_FUNCTION)
    variable_name = tk.StringVar(value = DEF_VARIABLE)
    start_value = tk.IntVar(value = DEF_START_VALUE)
    end_value = tk.IntVar(value = DEF_END_VALUE)
    num_points = tk.IntVar(value = DEF_PPU)