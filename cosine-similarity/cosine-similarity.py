import numpy as np

def cosine_similarity(a, b):
    n1 = np.linalg.norm(a)
    n2 = np.linalg.norm(b)
    if n1 == 0 or n2 == 0:
        return 0.0
    return np.dot(a, b) / (n1 * n2)