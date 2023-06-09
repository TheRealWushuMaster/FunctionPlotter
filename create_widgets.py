import tkinter as tk
import define_vars

def create_widgets(window, plot_function):
    # Create a label and entry field for the function input
    function_frame = tk.Frame(window)
    function_frame.pack()
    function_label = tk.Label(function_frame, text="Function: y = ")
    function_label.pack(side=tk.LEFT)
    function_entry = tk.Entry(function_frame, textvariable=define_vars.function_text)
    function_entry.pack(side=tk.LEFT)

        # Create a frame to hold the limit input fields
    limits_frame = tk.Frame(window)
    limits_frame.pack()

    # Create text entry fields for the limits
    limit_text = f"Limits of the {define_vars.variable_name.get()} variable:"
    limit_label = tk.Label(limits_frame, text=limit_text)
    limit_label.pack()
    start_label = tk.Label(limits_frame, text="Start: ")
    start_label.pack(side=tk.LEFT)
    start_entry = tk.Entry(limits_frame, textvariable=define_vars.start_value)
    start_entry.pack(side=tk.LEFT)
    end_label = tk.Label(limits_frame, text="End: ")
    end_label.pack(side=tk.LEFT)
    end_entry = tk.Entry(limits_frame, textvariable=define_vars.end_value)
    end_entry.pack(side=tk.LEFT)

    # Create a text entry for inputting the number of points to calculate
    points_frame = tk.Frame(window)
    points_frame.pack()
    points_label = tk.Label(points_frame, text="Points per unit: ")
    points_label.pack(side=tk.LEFT)
    points_entry = tk.Entry(points_frame, textvariable=define_vars.num_points)
    points_entry.pack(side=tk.LEFT)

    # Create a canvas for the plot
    canvas = tk.Canvas(window, width=711, height=300, bg="white")

    # Create a button to plot the function
    plot_button = tk.Button(window, text="Plot", command=lambda: plot_function(canvas))
    plot_button.pack()
    
    # Place the canvas
    canvas.pack()