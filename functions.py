import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from sympy import symbols, lambdify
import custom_functions
from scipy.integrate import trapz
import define_vars
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import tkinter as tk
from settings import *
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application

def verify_values(event=None, canvas=None, control=None):
    # Check if the expression entered contains the variable
    function = define_vars.function_text.get().lower()
    if not function.__contains__(define_vars.variable_name.get()):
        # If the variable is not present, add a dummy
        function += f"+0*{define_vars.variable_name.get()}"
    
    # Check if the input expression is valid
    if not validate_expression(function, define_vars.variable_name.get()):
        return
    
    # Check if the start and end values are correct
    try:
        if (define_vars.start_value.get() > define_vars.end_value.get()):
            temp = define_vars.start_value.get()
            define_vars.start_value.set(str(define_vars.end_value.get()))
            define_vars.end_value.set(temp)
    except:
        define_vars.start_value.set(DEF_START_VALUE)
        define_vars.end_value.set(DEF_END_VALUE)

    # Check if the resolution is a positive number
    try:
        if not define_vars.num_points.get() > 0:
            define_vars.num_points.set(DEF_PPU)
    except:
        define_vars.num_points.set(DEF_PPU)
    
    plot_math_function(function,
                       define_vars.variable_name.get(),
                       define_vars.start_value.get(),
                       define_vars.end_value.get(),
                       define_vars.num_points.get(),
                       canvas)
    if control:
        control.after(10, lambda: control.focus_set())

def validate_expression(expression, variable):
    try:
        x = sp.symbols(variable)
        sp.sympify(expression, evaluate=False)  # Parsing and validating the expression
        return True
    except Exception as e:
        tk.messagebox.showerror(title="Error found", message=f"Expression is invalid.\n{str(e)}")
        return False

def plot_math_function(expression, variable, start, end, num_points_per_unit, canvas):
    global x_vals, y_vals
    
    for widget in canvas.winfo_children():
        widget.destroy()

    points = num_points_per_unit * (end - start)
    x_vals = np.linspace(start, end, points)
    y_vals = evaluate_expression(expression, variable, x_vals)

    fig, ax = plt.subplots()
    ax.plot(x_vals, y_vals, color="red")
    ax.set_xlabel(variable)
    ax.set_ylabel("y")
    ax.set_title(f"$\it y = {define_vars.function_text.get()}$ with $\it x$ in [{start}, {end}]")
    ax.grid(visible=True, linestyle="--")

    canvas_plot = FigureCanvasTkAgg(fig, master=canvas)
    canvas_plot.draw_idle()
    canvas_widget = canvas_plot.get_tk_widget()
    canvas_widget.pack(fill=tk.BOTH, expand=True)
    
    toolbar = NavigationToolbar2Tk(canvas_plot, canvas, pack_toolbar=False)
    toolbar.update()
    toolbar.pack(side=tk.BOTTOM, fill=tk.X)

def evaluate_expression(expression, variable, x_vals):
    error = None
    x = symbols(variable)
    try:
        expr = parse_expression(expression, variable)
        f = lambdify(x, expr, modules=['numpy', custom_functions.get_custom_functions()])
        y = f(x_vals)
    except Exception:
        tk.messagebox.showerror(title="Error", message=str(Exception))
    return y

def parse_expression(expression, variable):
    valid_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
    parsed_expr = ''
    for char in expression:
        if char in valid_chars or char in '()[]*+-/.,':
            parsed_expr += char
        elif char == '^':
            parsed_expr += '**'
    parsed_expr = parsed_expr.replace(variable, 'x')
    return parsed_expr

def on_click(event):
    global x_start
    if event.button == 1 and event.inaxes is not None:
        x_start = event.xdata
        plt.gca().set_autoscale_on(True)
        plt.gcf().canvas.mpl_disconnect(event)
        plt.gcf().canvas.mpl_connect('motion_notify_event', on_drag)
        plt.gcf().canvas.mpl_connect('button_release_event', on_release)

def on_drag(event):
    global x_end
    if event.button == 1:
        x_end = event.xdata
        #plt.gca().lines[-1].set_xdata([x_start, x_end])
        #plt.gca().figure.canvas.draw()

        if x_start > x_end:
            start = x_end
            end = x_start
        else:
            start = x_start
            end = x_end
        
        x_vals_selected = x_vals[(x_vals >= start) & (x_vals <= end)]
        y_vals_selected = y_vals[(x_vals >= start) & (x_vals <= end)]
        
        integral = trapz(y_vals_selected, x_vals_selected)
        print(f'Integral = {integral}')

        # Fill the area under the curve
        plt.fill_between(x_vals_selected, y_vals_selected, alpha=0.5, color="darkgreen")

        plt.draw()

def on_release(event):
    
    # Reset the x_start variable to None
    x_start = None
    x_end = None
    plt.clf()
    plot_math_function(define_vars.function_text.get(),
                       define_vars.variable_name.get(),
                       define_vars.start_value.get(),
                       define_vars.end_value.get(),
                       define_vars.num_points.get())