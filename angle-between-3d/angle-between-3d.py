import numpy as np

def angle_between_3d(v, w):
    n1 = np.linalg.norm(v)
    n2 = np.linalg.norm(w)
    return np.arccos(np.dot(v, w) / (n1 * n2))