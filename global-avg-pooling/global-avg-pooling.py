import numpy as np

def global_avg_pool(x):
    """
    Compute global average pooling over spatial dims.
    Supports (C,H,W) => (C,) and (N,C,H,W) => (N,C).
    """
    x = np.array(x)
    if len(x.shape) < 3:
        raise ValueError()
    return np.mean(x, axis=(-1, -2))