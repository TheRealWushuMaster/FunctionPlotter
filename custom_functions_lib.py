import numpy as np
from math import e

def get_custom_functions():
    custom_functions = {'step':     step_function,
                        'pulse':    pulse_function,
                        'relu':     relu_function,
                        'sigmoid':  sigmoid_function,
                        'sign':     sign_function,
                        'normal':   normal_function}
    return custom_functions

def step_function(x):
    return np.where(x < 0, 0, 1)

def pulse_function(x):
    return np.where((x >= 0) & (x <= 1), 1, 0)

def relu_function(x):
    return np.where(x < 0, 0, x)

def sigmoid_function(x):
    return 1/(1 + e**(-x))

def sign_function(x):
    return np.where(x < 0, -1, 1)

def normal_function(x):
    return e**(-x**2)