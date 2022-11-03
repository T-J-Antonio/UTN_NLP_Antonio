from stemmer import WrappedVectorizer
from textract import process
from functools import reduce

# textract has problems interacting with cmd, use bash with -i flag+

# Returns a list of tuples:
#   1st element: original sentence.
#   2nd element: tokenized, stemmmed sentence, without stop words.
def processed_sentences_from_file(src):
    sentences = sentences_from_file(src)
    vectorizer = WrappedVectorizer()
    analyze = vectorizer.build_analyzer()
    stemmed_sentences = list(map(lambda s: (s, analyze(s)), sentences))
    non_empty_sentences = list(filter(lambda t: t[1] != [] and t[0] != "", stemmed_sentences))
    sentences_without_unknown = list(map(lambda t: (t[0].replace("\ufffd", "_"), t[1]), non_empty_sentences))
    return sentences_without_unknown

# Obtains a list of sentences.
def sentences_from_file(src):
    text = process(src).decode("utf-8")
    sentence_list = split_by_punctuation_symbols(text)
    return sentence_list

def concat(list_of_lists):
    return reduce(lambda list1, list2: list1 + list2, list_of_lists, [])

def split_by_punctuation_symbols(string):
    split_by_full_stops = string.split(".")
    split_by_question_marks = concat(list(map(lambda s: s.split("?"), split_by_full_stops)))
    split_by_enter = concat(list(map(lambda s: s.split("\n"), split_by_question_marks)))
    split_by_tab = concat(list(map(lambda s: s.split("\t"), split_by_enter)))
    return split_by_tab