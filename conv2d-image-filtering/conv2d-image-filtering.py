import numpy as np


def conv2d(image, kernel, stride=1, padding=0):
    """
    Apply 2D convolution to a single-channel image.
    """
    image = np.array(image)
    kernel = np.array(kernel)
    h, w = image.shape
    kh, kw = kernel.shape
    padded = np.zeros((h + 2 * padding, w + 2 * padding))
    padded[padding : padding + h, padding : padding + w] = image

    h_out = (h + 2 * padding - kh) // stride + 1
    w_out = (w + 2 * padding - kw) // stride + 1
    out = np.zeros((h_out, w_out))

    for x in range(w_out):
        for y in range(h_out):
            out[y][x] = (padded[y * stride: y * stride + kh, x * stride : x * stride + kw] * kernel).sum()
    return out.tolist()