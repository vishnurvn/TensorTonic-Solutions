def top_k_recommendations(scores, rated_indices, k):
    scores_idxs = [(val, i) for i, val in enumerate(scores)]
    scores_idxs = filter(lambda x: x[1] not in rated_indices, scores_idxs)
    scores_idxs = sorted(scores_idxs, key=lambda x: x[0], reverse=True)
    return [v[1] for v in scores_idxs[0:k]]