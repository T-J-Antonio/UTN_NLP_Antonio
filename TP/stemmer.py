from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem import SnowballStemmer
from nltk import word_tokenize
from textract import process

# Wraps SpanishStemmerCountVectorizer with the spanish stop words to provide a cleaner interface
class WrappedVectorizer():
    def count_vectorizer(_):
        spanish_stop_words = word_tokenize(bytes.decode(process("stop_words.txt")))
        return SpanishStemmedCountVectorizer(stop_words = spanish_stop_words)
    def build_analyzer(self): 
        return self.count_vectorizer().build_analyzer()

class SpanishStemmedCountVectorizer(CountVectorizer):
    def build_analyzer(self):
        spanish_stemmer = StemmerBuilder().build_spanish_stemmer()
        analyzer = super(SpanishStemmedCountVectorizer, self).build_analyzer()
        return lambda doc: list(map(lambda w: spanish_stemmer.stem(w), analyzer(doc)))

class StemmerBuilder():
    def build_spanish_stemmer(_): return SnowballStemmer("spanish")