import numpy as np

def manhattan_distance(x, y):
    return float(np.abs(np.subtract(x, y)).sum())