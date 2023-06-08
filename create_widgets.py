import tkinter as tk

def create_widgets(window, plot_function, function_expression,
                   start_value, end_value, num_points):
    # Create a label and entry field for the function input
    function_frame = tk.Frame(window)
    function_frame.pack()
    function_label = tk.Label(function_frame, text="Function: y = ")
    function_label.pack(side=tk.LEFT)
    function_entry = tk.Entry(function_frame)
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
    start_entry = tk.Entry(limits_frame)
    start_entry.pack(side=tk.LEFT)
    end_label = tk.Label(limits_frame, text="End: ")
    end_label.pack(side=tk.LEFT)
    end_entry = tk.Entry(limits_frame)
    end_entry.pack(side=tk.LEFT)
    
    # Create a button to plot the function
    plot_button = tk.Button(window, text="Plot", command=plot_function)
    plot_button.pack()
    
    # Create a canvas for the plot
    #result_label = tk.Label(window, text="Plot:")
    #result_label.pack()
    canvas = tk.Canvas(window, width=711, height=300, bg="white")
    canvas.pack()