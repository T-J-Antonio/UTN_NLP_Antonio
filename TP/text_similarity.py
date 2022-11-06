from sklearn.metrics.pairwise import cosine_similarity
from stemmer import WrappedVectorizer

def text_similarity(text1, text2):
    vectorizer = WrappedVectorizer()
    sparse_matrix = vectorizer.fit_transform([text1, text2])
    return cosine_similarity(sparse_matrix)[0][1]
