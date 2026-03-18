import numpy as np

def entropy_node(y):
    y = np.array(y)
    entropy = 0.0
    for c in np.unique(y):
        p = (y == c).sum() / len(y)
        entropy += np.log2(p) * p
    return -entropy