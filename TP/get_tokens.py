from stemmer import WrappedVectorizer
from textract import process
from functools import reduce

# textract has trouble interacting with cmd, use bash with -i flag

def sentences_from_file(src):
    text = text_from_file(src)
    sentence_list = split_by_punctuation_symbols(text)
    sentence_list_filtered = list(filter(lambda s: s != "", sentence_list))
    return sentence_list_filtered

def concat(list_of_lists):
    return reduce(lambda list1, list2: list1 + list2, list_of_lists, [])

def split_by_punctuation_symbols(string):
    split_by_full_stops = string.split(".")
    split_by_question_marks = concat(list(map(lambda s: s.split("?"), split_by_full_stops)))
    split_by_enter = concat(list(map(lambda s: s.split("\n"), split_by_question_marks)))
    split_by_tab = concat(list(map(lambda s: s.split("\t"), split_by_enter)))
    return split_by_tab

def text_from_file(src):
    return process(src).decode("utf-8")

def tokens_from_file(src):
    text = process(src).decode("utf-8")
    vectorizer = WrappedVectorizer()
    analyze = vectorizer.build_analyzer()
    tokens = analyze(text)
    return tokens