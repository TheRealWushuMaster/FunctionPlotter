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
    
    # Create a label for the limits input
    limits_label = tk.Label(window, text="Limits:")
    limits_label.pack()

    # Create a frame to hold the limit input fields
    limits_frame = tk.Frame(window)
    limits_frame.pack()
    
    # Create text entry fields for the limits
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
    points_label = tk.Label(points_frame, text="Number of points: ")
    points_label.pack(side=tk.LEFT)
    points_entry = tk.Entry(points_frame, textvariable=define_vars.num_points)
    points_entry.pack(side=tk.LEFT)

    # Create a button to plot the function
    plot_button = tk.Button(window, text="Plot", command=lambda: plot_function(define_vars.function_text.get(),
                                                                               define_vars.variable_name.get(),
                                                                               define_vars.start_value.get(),
                                                                               define_vars.end_value.get(),
                                                                               define_vars.num_points.get()))
    plot_button.pack()
    
    # Create a canvas for the plot
    #result_label = tk.Label(window, text="Plot:")
    #result_label.pack()
    canvas = tk.Canvas(window, width=711, height=300, bg="white")
    canvas.pack()