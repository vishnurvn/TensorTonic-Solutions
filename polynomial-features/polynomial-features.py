import numpy as np

def polynomial_features(values, degree):
    arr = np.zeros((len(values), degree + 1))
    for idx, v in enumerate(values):
        for pow in range(degree + 1):
            arr[idx][pow] = np.pow(v, pow)
    return arr.tolist()