import numpy as np
from math import e

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