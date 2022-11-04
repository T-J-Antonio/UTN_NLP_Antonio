import sys
from get_tokens import processed_sentences_from_file
from get_files_from_dataset import get_files_from_dataset
from text_similarity import similar_sentences

# PDF files cannot include special characters in their names
file_list = get_files_from_dataset()

text_list = list(map(processed_sentences_from_file, file_list))

file = sys.argv[1]
print(file)
text_to_analyze = processed_sentences_from_file(file)

plagiarism = list(map(lambda t: (t[0], []), text_to_analyze))

for i in range(0, len(file_list)):
    plagiarised_sentences = similar_sentences(text_to_analyze, text_list[i])
    for j in range(0, len(text_to_analyze)):
        if (plagiarised_sentences[j]): plagiarism[j][1].append(file_list[i])

print("Nombre del archivo: " + file)
for s in plagiarism:
    print("Oración: " + s[0])
    if s[1] == []: print("No plagiada.")
    else:
        print("Posiblemente plagiada de las siguientes fuentes:")
        for ps in s[1]: print(ps.replace("\u0301", "_"))