import numpy as np


def sobel_edges(image):
    im = np.array(image)
    h, w = im.shape
    H, W = h + 2, w + 2
    padded_im = np.zeros((H, W))
    padded_im[1 : 1 + h, 1 : 1 + w] = image
    Gx = np.zeros_like(im)
    Gy = np.zeros_like(im)

    kx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])

    ky = kx.T

    for y in range(H - 2):
        for x in range(W - 2):
            Gx[y][x] = (padded_im[y : y + 3, x : x + 3] * kx).sum()
            Gy[y][x] = (padded_im[y : y + 3, x : x + 3] * ky).sum()
    G = np.sqrt(np.square(Gx) + np.square(Gy))
    return G.tolist()

    