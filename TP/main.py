from get_tokens import processed_sentences_from_file
from sentence_similarity import sentence_similarity
from get_files_from_dataset import get_files_from_dataset

file_list = get_files_from_dataset()

text_list = list(map(processed_sentences_from_file, file_list))

similar_sentences = []

for t in text_list[0]:
    for t2 in text_list[1]:
        similarity = sentence_similarity(t[1], t2[1])
        if (similarity > 0.3):
            similar_sentences.append((t[0], t2[0]))
            print(t[1])
            print(t2[1])

for t in similar_sentences:
    print(t[0] + "; " + t[1])