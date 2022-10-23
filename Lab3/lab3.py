from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem import SnowballStemmer
from nltk import word_tokenize
from textract import process
from functools import reduce

spanish_stemmer = SnowballStemmer("spanish")

class SpanishStemmedCountVectorizer(CountVectorizer):
    def build_analyzer(self):
        analyzer = super(SpanishStemmedCountVectorizer, self).build_analyzer()
        return lambda doc: list(map(lambda w: spanish_stemmer.stem(w), analyzer(doc)))

spanish_stop_words = word_tokenize(bytes.decode(process("stop_words.txt")))
# Fuente de la lista de stop words: https://www.ranks.nl/stopwords/spanish
# Referido a su vez en: http://ceur-ws.org/Vol-1881/COSET_paper_3.pdf

vectorizer = SpanishStemmedCountVectorizer(stop_words = spanish_stop_words)
analyze = vectorizer.build_analyzer()

def concat_strings(list_of_strings):
    return reduce(lambda str1, str2: str1 + str2, list_of_strings, "")

sentence = "Las partes del discurso son las categorías sintácticas a las que corresponden las palabras."
analysis = analyze(sentence)
print("Ejemplo 1:")
for w in analysis: print(w)
# Output: 
# part
# del
# discurs
# son
# categor
# sintact
# que
# correspond
# palabr


sentence = """La clasificación consiste en categorizar un conjunto de palabras, un texto, etc., entre
            cierto conjunto de posibles etiquetas."""
analysis = analyze(sentence)
print("Ejemplo 2:")
for w in analysis: print(w)
# Output:
# clasif
# cons
# categoriz
# conjunt
# de
# palabr
# text
# etc
# conjunt
# de
# posibl
# etiquet

# Corpus: Constitución de la Nación Argentina.
# Fuente: https://biblioteca.org.ar/libros/201250.pdf
full_text = bytes.decode(process("constitution_of_the_argentine_nation.pdf"))
pages = full_text.split("\x0c")
corpus_pages = pages[1:47]
corpus = concat_strings(corpus_pages)

analysis = analyze(corpus)
print("Corpus:")
for w in analysis: print(w)