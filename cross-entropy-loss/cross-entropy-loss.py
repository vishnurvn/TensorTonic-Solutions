import numpy as np

def cross_entropy_loss(y_true, y_pred):
    one_hot = np.eye(np.max(y_true) + 1)[y_true]
    return -np.sum(one_hot * np.log(y_pred), axis=-1).mean()