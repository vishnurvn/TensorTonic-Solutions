import numpy as np

def apply_homogeneous_transform(T, points):
    points = np.array(points).reshape(-1, 3)
    r, _ = points.shape
    points = np.hstack([points, np.ones((points.shape[0], 1))])
    out = np.matmul(T, points.T).T[..., 0: 3]
    if r == 1:
        return out.flatten()
    return out