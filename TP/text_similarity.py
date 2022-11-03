from sentence_similarity import sentence_similarity

def amount_of_similar_sentences(text1, text2):
    amount = 0
    for sentence1 in text1:
        for sentence2 in text2:
            if sentence_similarity(sentence1[1], sentence2[1]) > 0.3: 
                amount += 1
                break
    return amount

def text_similarity(new_text, text_from_dataset):
    coincidences = amount_of_similar_sentences(new_text, text_from_dataset)
    percentage = coincidences / len(new_text)
    return percentage