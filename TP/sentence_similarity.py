# Recieves two tokenized, stemmed sentences, and returns how similar they are.
# Similarity is defined as a value between 0 and 1 that is equal to the amount of
# repeated types in both sentences divided by the total amount of types.
def sentence_similarity(sentence1, sentence2):
    sentence1_types = set(sentence1)
    sentence2_types = set(sentence2)
    coincidences = len(sentence1_types.intersection(sentence2_types))
    amount_of_types = len(sentence1_types.union(sentence2_types))
    similarity = coincidences / amount_of_types
    return similarity
