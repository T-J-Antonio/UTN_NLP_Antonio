import sys
from get_tokens import processed_sentences_from_file
from get_files_from_dataset import get_files_from_dataset
from text_similarity import text_similarity

# PDF files cannot include special characters in their names
file_list = get_files_from_dataset()

text_list = list(map(processed_sentences_from_file, file_list))

file = sys.argv[1]
print(file)
text_to_analyze = processed_sentences_from_file(file)

for i in range(0, len(file_list)):
    result = text_similarity(text_to_analyze, text_list[i])
    if result > 0.3: 
        print(file_list[i].replace("\u0301", "_"))
        print(result)