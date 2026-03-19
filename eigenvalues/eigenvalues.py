import numpy as np

def calculate_eigenvalues(matrix):
    try:
        matrix = np.array(matrix)
    except:
        return None
    if matrix.ndim != 2:
        return None
    if matrix.shape[0] != matrix.shape[1]:
        return None
    eigen = np.linalg.eigvals(matrix)
    return eigen