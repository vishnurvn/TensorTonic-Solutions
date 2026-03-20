def precision_recall_at_k(recommended, relevant, k):
    top_k = recommended[0: k]
    items = []
    for item in top_k:
        if item in relevant:
            items.append(item)
    return [len(items) / k, len(items) / len(relevant)]