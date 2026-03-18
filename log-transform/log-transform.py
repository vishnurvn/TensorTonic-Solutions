import numpy as np

def log_transform(values):
    return np.log(np.add(values, 1))