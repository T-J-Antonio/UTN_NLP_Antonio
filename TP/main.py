import sys
from get_tokens import text_from_file
from get_files_from_dataset import get_files_from_dataset
from text_similarity import text_similarity
from tag_topic import tag_topic

# PDF files cannot include special characters in their names
file_list = get_files_from_dataset()

file = sys.argv[1]

topic = tag_topic(file)

text_to_analyze = text_from_file(file)

plagiarised_texts = []

for f in file_list:
    similarity = text_similarity(text_to_analyze, text_from_file(f))
    if similarity > 0.9: plagiarised_texts.append(f)

print("Nombre del archivo: " + file)
print("Tópico del archivo: " + topic)
for f in plagiarism:
    print(f.replace("\u0301", "_"))