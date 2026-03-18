import numpy as np


def target_encoding(categories, targets):
    categories = np.array(categories)
    targets = np.array(targets)
    new_targets = np.zeros_like(targets, dtype=np.float32)

    for c in np.unique(categories):
        mask = categories == c
        new_targets[mask] = targets[mask].mean()
    return new_targets.tolist()