import numpy as np

def poisson_pmf_cdf(lam, k):
    pmf = np.exp(-lam) * np.pow(lam, k) / np.prod(np.arange(1, k + 1))
    cdf = 0
    for i in range(k + 1):
        cdf += np.exp(-lam) * np.pow(lam, i) / np.prod(np.arange(1, i + 1))
    return pmf, cdf