import nltk
from nltk import word_tokenize
from nltk.corpus import brown

def pos_according_to_tagger(sentence, word, tagger):
    tokens = word_tokenize(sentence)
    tagged_tokens = tagger.tag(tokens)
    # Se asume que la palabra aparece una vez en la oración
    word_with_pos = list(filter(lambda t: t[0] == word, tagged_tokens))[0]
    pos = word_with_pos[1]
    return pos


# Punto 3

nltk.help.upenn_tagset("VB*")
# Al imprimir esto en pantalla, se ve que hay 6 categorías de verbos en el tagset Penn.
print("\n")

nltk.help.upenn_tagset("NN*")
# Al imprimir esto en pantalla, se ve que hay 4 categorías de sustantivos en el tagset Penn.
# NN: sustantivo común singular o colectivo
# NNP: sustantivo propio singular
# NNS: sustantivo común plural
# NNPS: sustantivo propio plural
print("\n")

nltk.help.brown_tagset("VB*")
# Al imprimir esto en pantalla, se ve que hay 14 categorías de verbos en el tagset Brown.
print("\n")

nltk.help.brown_tagset("NN*")
# Al imprimir esto en pantalla, se ve que hay 27 categorías de sustantivos en el tagset Brown.
print("\n")

# Punto 5

race_as_noun = ("race", "NN")
race_as_verb = ("race", "VB")

print("La longitud del corpus Brown es: " + str(len(brown.tagged_words())))
# respuesta: 1161192

times_race_is_noun = brown.tagged_words().count(race_as_noun)
times_race_is_verb = brown.tagged_words().count(race_as_verb)

print("Es más frecuente como verbo" if times_race_is_verb > times_race_is_noun else "Es más frecuente como sustantivo")
# respuesta: es más frecuente como verbo

# Punto 6

sentence = "The Secretariat is expected to race tomorrow"

unigram_tagger = nltk.tag.UnigramTagger(brown.tagged_sents(categories="news")[:5000])

hmm_tagger = nltk.hmm.HiddenMarkovModelTrainer().train_supervised(brown.tagged_sents(categories="news")[:5000])

tag_according_to_unigram = pos_according_to_tagger(sentence, "race", unigram_tagger)
tag_according_to_hmm = pos_according_to_tagger(sentence, "race", hmm_tagger)

print("Según el tagger unigramo, la palabra \"race\" es: " + tag_according_to_unigram)
# respuesta: NN
print("Según el tagger HMM, la palabra \"race\" es: " + tag_according_to_hmm)
# respuesta: VB (es la correcta en este contexto)
