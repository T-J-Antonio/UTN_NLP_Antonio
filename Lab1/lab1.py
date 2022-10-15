from nltk.book import *
from nltk import re

def lower_and_filter(a_list):
    list_lower = list(map(lambda w: w.lower(), a_list))
    list_filtered = list(filter(lambda w: re.search("\w", w), list_lower))
    return list_filtered

def type_token_ratio(tokens):
    types = set(tokens)
    return len(types) / len(tokens)

def unigram_mle(tokens, word):
    word_count = tokens.count(word)
    return word_count / len(tokens)
    # fuente de método count(): https://www.datasciencelearner.com/python-built-in-functions-lists/

# Punto 1
moby_dick_tokens = lower_and_filter(text1.tokens)
moby_dick_number_of_tokens = len(moby_dick_tokens)
print("Moby Dick tiene " + str(moby_dick_number_of_tokens) + " tokens.") 
# respuesta: 218621

# Punto 2
moby_dick_types = set(moby_dick_tokens)
moby_dick_number_of_types = len(moby_dick_types)
print("Moby Dick tiene " + str(moby_dick_number_of_types) + " types.") 
# respuesta: 17140

# Punto 3
moby_dick_type_token_ratio = type_token_ratio(moby_dick_tokens)
print("El type-token ratio de Moby Dick es " + str(moby_dick_type_token_ratio)) 
# respuesta: 0,078

# Punto 4
wsj_tokens = lower_and_filter(text7.tokens)
wsj_type_token_ratio = type_token_ratio(wsj_tokens)
print("El type-token ratio del WSJ es " + str(wsj_type_token_ratio)) 
# respuesta: 0,130

# Punto 5
print("Moby Dick es más diverso" if (moby_dick_type_token_ratio > wsj_type_token_ratio) else "El WSJ es más diverso")
# fuente de sintaxis del operador ternario: https://www.pythontutorial.net/python-basics/python-ternary-operator/
# respuesta: el WSJ es más diverso

# Punto 7
mle_whale_moby_dick = unigram_mle(moby_dick_tokens, "whale")
print("El MLE de \"whale\" en Moby Dick es " + str(mle_whale_moby_dick))
# respuesta: 0,006

# Punto 8
mle_whale_wsj = unigram_mle(wsj_tokens, "whale")
print("El MLE de \"whale\" en Moby Dick es " + str(mle_whale_wsj))
# respuesta: 0