import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, lambdify
from scipy.integrate import quad
import custom_functions_lib
from scipy.integrate import trapz

def plot_math_function(expression, variable, start, end, num_points):
    global x_vals, y_vals
    x_vals = np.linspace(start, end, num_points)
    y_vals = evaluate_expression(expression, variable, x_vals)

    plt.plot(x_vals, y_vals, color="red")
    plt.xlabel(variable)
    plt.ylabel('y')
    plt.title('Plot of ' + expression)
    plt.grid(visible=True, linestyle="--")

    # Enable interactive mode for selecting range
    plt.gca().set(xlim=(start, end), ylim=(np.min(y_vals), np.max(y_vals)))
    plt.gca().set_ymargin(0.1)
    plt.gca().set_autoscale_on(False)

    # Connect the mouse event to the handler function
    plt.gcf().canvas.mpl_connect('button_press_event', on_click)
    plt.gca().figure.canvas.draw()

    plt.show()

def evaluate_expression(expression, variable, x_vals):
    x = symbols(variable)
    expr = parse_expression(expression, variable)
    f = lambdify(x, expr, modules=['numpy', get_custom_functions()])
    y = f(x_vals)
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

def get_custom_functions():
    custom_functions = {'step':     custom_functions_lib.step_function,
                        'pulse':    custom_functions_lib.pulse_function,
                        'relu':     custom_functions_lib.relu_function,
                        'sigmoid':  custom_functions_lib.sigmoid_function,
                        'sign':     custom_functions_lib.sign_function,
                        'normal':   custom_functions_lib.normal_function}
    return custom_functions

def on_click(event):
    global x_start
    if event.button == 1 and event.inaxes is not None:
        x_start = event.xdata
        print(f"x_start = {x_start}")
        plt.gca().set_autoscale_on(True)
        plt.gcf().canvas.mpl_disconnect(event)
        plt.gcf().canvas.mpl_connect('motion_notify_event', on_drag)
        plt.gcf().canvas.mpl_connect('button_release_event', on_release)

def on_drag(event):
    global x_end
    if event.button == 1:
        x_end = event.xdata
        #plt.gca().lines[-1].set_xdata([x_start, x_end])
        plt.gca().figure.canvas.draw()

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
        plt.fill_between(x_vals_selected, y_vals_selected, alpha=1, color="darkgreen")

        plt.draw()
    # if event.inaxes is not None:
    #     x_end = event.xdata
    #     print(f"x_end = {x_end}")
    #     plt.gca().lines[-1].set_xdata([x_start, x_end])
    #     #plt.gca().figure.canvas.draw()

def on_release(event):
    
    # Reset the x_start variable to None
    x_start = None
    x_end = None
    plt.clf()
    plot_math_function(input_expression, variable_name, start_value, end_value, num_points)
    
    # if event.button == 1:
    #     plt.gcf().canvas.mpl_disconnect(event)
    #     plt.gcf().canvas.mpl_disconnect('motion_notify_event')
    #     plt.gca().lines[-1].set_xdata([x_start, event.xdata])
    #     plt.gca().figure.canvas.draw()

    #     x_vals = np.linspace(x_start, event.xdata, 100)
    #     y_vals = evaluate_expression(input_expression, variable_name, x_vals)
    #     integral_value, _ = quad(evaluate_expression, x_start, event.xdata, args=(variable_name, x_vals))

    #     print("Integral value:", integral_value)

    #     # Highlight the selected range
    #     plt.fill_between(x_vals, 0, y_vals, where=(x_vals >= x_start) & (x_vals <= event.xdata), alpha=0.3)

    #     plt.show()

# Example usage
input_expression = "sin(2*x)/x"
variable_name = "x"
start_value = -5
end_value = 5
num_points = 1000

input_expression = input_expression.lower()  # Convert input expression to lowercase

plot_math_function(input_expression, variable_name, start_value, end_value, num_points)
