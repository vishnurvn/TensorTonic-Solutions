def weighted_moving_average(values, weights):
    """
    Compute the weighted moving average using the given weights.
    """
    final_vals = []
    for idx in range(len(values) - len(weights) + 1):
        s = 0
        for v, w in zip(values[idx: ], weights):
            s += v * w
        final_vals.append(s / sum(weights))
    return final_vals
            