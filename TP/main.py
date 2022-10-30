from get_tokens import processed_sentences_from_file
from sentence_similarity import sentence_similarity

text = processed_sentences_from_file(a_src)
text2 = processed_sentences_from_file(a_src)

similar_sentences = []

for t in text:
    for t2 in text2:
        similarity = sentence_similarity(t[1], t2[1])
        if (similarity > 0.3):
            similar_sentences.append((t[0], t2[0]))
            print(t[1])
            print(t2[1])

for t in similar_sentences:
    print(t[0] + "; " + t[1])