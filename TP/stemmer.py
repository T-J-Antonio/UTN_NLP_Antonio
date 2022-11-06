from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem import SnowballStemmer
from nltk import word_tokenize
from textract import process

# Wraps SpanishStemmerCountVectorizer with the spanish stop words to provide a cleaner interface
class WrappedVectorizer():
    def count_vectorizer(self):
        spanish_stop_words = word_tokenize(process("stop_words.txt").decode("utf-8"))
        return SpanishStemmedCountVectorizer(stop_words = spanish_stop_words)
    def build_analyzer(self): 
        return self.count_vectorizer().build_analyzer()
    def fit_transform(self, texts):
        return self.count_vectorizer().fit_transform(texts)

class SpanishStemmedCountVectorizer(CountVectorizer):
    def build_analyzer(self):
        spanish_stemmer = StemmerBuilder().build_spanish_stemmer()
        analyzer = super(SpanishStemmedCountVectorizer, self).build_analyzer()
        return lambda doc: list(map(lambda w: spanish_stemmer.stem(w), analyzer(doc)))

class StemmerBuilder():
    def build_spanish_stemmer(self): return SnowballStemmer("spanish")