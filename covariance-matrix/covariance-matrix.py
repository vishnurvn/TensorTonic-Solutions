import numpy as np

def covariance_matrix(X):
    arr = np.array(X, dtype=float)
    if arr.ndim < 2:
        return None
    if len(X) == 1:
        return None
    if np.isnan(arr).all():
        return None
    mean_cols = arr.mean(axis=0, keepdims=True)
    centered = arr - mean_cols
    cov = centered.T @ centered / (len(arr) - 1)
    return cov