def word_count_dict(sentences):
    d = dict()
    for sentence in sentences:
        print(d)
        for word in sentence:
            if word not in d:
                d[word] = 1
            else:
                d[word] += 1
    return d