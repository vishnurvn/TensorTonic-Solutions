import numpy as np

def dice_loss(p, y, eps=1e-8):
    p = np.array(p)
    y = np.array(y)
    num = 2 * (p * y).sum() + eps
    den = p.sum() + y.sum() + eps
    return 1 - num / den