import numpy as np

def rolling_std(values, window_size):
    values = np.array(values)
    stds = []
    for idx in range(len(values) - window_size + 1):
        r_mean = values[idx: idx + window_size].sum() / window_size
        r_var = np.square(values[idx: idx + window_size] - r_mean).sum() / window_size
        r_std = np.sqrt(r_var)
        stds.append(r_std)
    return stds