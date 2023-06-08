import tkinter as tk

function_text = tk.StringVar()
function_text.set("sin(2*x)/x")

variable_name = tk.StringVar()
variable_name.set("x")

start_value = tk.IntVar()
start_value.set(-5)

end_value = tk.IntVar()
end_value.set(5)

num_points = tk.IntVar()
num_points.set(1000)