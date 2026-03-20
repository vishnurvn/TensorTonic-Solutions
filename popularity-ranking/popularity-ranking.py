def popularity_ranking(items, min_votes, global_mean):
    """
    Compute the Bayesian weighted rating for each item.
    """
    ranks = []
    for r, v in items:
        wr = v / (v + min_votes) * r + min_votes / (v + min_votes) * global_mean
        ranks.append(wr)
    return ranks