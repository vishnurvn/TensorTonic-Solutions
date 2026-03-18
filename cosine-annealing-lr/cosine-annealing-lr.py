import numpy as np

def cosine_annealing_schedule(base_lr, min_lr, total_steps, current_step):
    lr = min_lr + (base_lr - min_lr) * (1 + np.cos(np.pi * current_step / total_steps)) / 2
    return lr