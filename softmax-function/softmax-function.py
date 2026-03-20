import numpy as np

def softmax(x):
    arr = np.asarray(x)
    arr = arr - np.max(arr, axis=-1, keepdims=True)
    return np.exp(arr) / np.sum(np.exp(arr), axis=-1, keepdims=True)