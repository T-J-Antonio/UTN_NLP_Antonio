from sentence_similarity import sentence_similarity

def find_similarity(sentence, text):
    for sentence_from_text in text:
        if sentence_similarity(sentence[1], sentence_from_text[1]) > 0.5: return True
    return False

def similar_sentences(new_text, text_from_dataset):
    mapped = list(map(lambda sentence: find_similarity(sentence, text_from_dataset), new_text))
    return mapped

def text_similarity(new_text, text_from_dataset):
    coincidences = similar_sentences(new_text, text_from_dataset)
    percentage = coincidences / len(new_text)
    return percentage