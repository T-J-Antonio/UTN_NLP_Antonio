from stemmer import WrappedVectorizer
from nltk import word_tokenize, re
from textract import process
from sentence_similarity import sentence_similarity

# textract has problems interacting with cmd, use bash with -i flag
def tokens_from_file(src):
    text = bytes.decode(process(src))
    tokens = lower_and_filter(word_tokenize(text))
    return tokens

def lower_and_filter(a_list):
    list_lower = list(map(lambda w: w.lower(), a_list))
    list_filtered = list(filter(lambda w: re.search("\w", w), list_lower))
    return list_filtered

# Obtains a list of tokenized, stemmmed sentences, without stop words.
def processed_sentences_from_file(src):
    sentences = sentences_from_file(src)
    vectorizer = WrappedVectorizer()
    analyze = vectorizer.build_analyzer()
    stemmed_sentences = list(map(lambda s: analyze(s), sentences))
    return stemmed_sentences

# Obtains a list of sentences.
def sentences_from_file(src):
    text = bytes.decode(process(src))
    return text.split(".")