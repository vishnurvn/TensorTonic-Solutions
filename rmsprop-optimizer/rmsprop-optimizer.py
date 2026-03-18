import numpy as np

def rmsprop_step(w, g, s, lr=0.001, beta=0.9, eps=1e-8):
    g = np.array(g)
    s_t = beta * np.array(s) + (1 - beta) * np.square(g)
    w = w - lr * g / (np.sqrt(s_t + eps))
    return w, s_t