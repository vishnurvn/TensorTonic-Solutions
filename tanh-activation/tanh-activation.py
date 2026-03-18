import numpy as np

def tanh(x):
    x = np.array(x)
    num = np.exp(x) - np.exp(-x)
    den = np.exp(x) + np.exp(-x)
    return num / den