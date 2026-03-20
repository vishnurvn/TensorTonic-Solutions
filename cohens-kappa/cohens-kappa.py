import numpy as np

def cohens_kappa(rater1, rater2):
    r1 = np.asarray(rater1)
    r2 = np.asarray(rater2)
    n = len(rater1)

    p0 = (r1 == r2).sum() / n
    labels = np.unique(rater1 + rater2)


    pe = 0
    for l in labels:
        pei = (r1 == l).sum() / n * (r2 == l).sum() / n
        pe += pei

    if pe == 1:
        return 1
    return (p0 - pe) / (1 - pe)