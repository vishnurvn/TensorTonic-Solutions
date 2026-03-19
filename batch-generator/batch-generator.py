import numpy as np
import math

def batch_generator(X, y, batch_size, rng=None, drop_last=False):
    indices = np.arange(len(X))
    if rng:
        rng.shuffle(indices)
    else:
        np.random.shuffle(indices)

    last_batch = math.ceil(len(indices) / batch_size)
    if drop_last:
        last_batch -= 1

    for bidx in range(last_batch):
        X_, y_ = [], []
        idxs = indices[bidx * batch_size: (bidx + 1) * batch_size]
        for idx in idxs:
            X_.append(X[idx])
            y_.append(y[idx])
        yield np.array(X_), np.array(y_)