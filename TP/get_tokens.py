from nltk import word_tokenize, re
from textract import process

# textract has problems interacting with cmd, use bash with -i flag
def tokens_from_file(src):
    text = process(src)
    tokens = lower_and_filter(word_tokenize(text))
    return tokens

def lower_and_filter(a_list):
    list_lower = list(map(lambda w: w.lower(), a_list))
    list_filtered = list(filter(lambda w: re.search("\w", w), list_lower))
    return list_filtered