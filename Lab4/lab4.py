import nltk
from nltk.wsd import lesk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import brown

def pos_according_to_tagger(sentence, word, tagger):
    tokens = word_tokenize(sentence)
    tagged_tokens = tagger.tag(tokens)
    # Se asume que la palabra aparece una vez en la oración
    word_with_pos = list(filter(lambda t: t[0] == word, tagged_tokens))[0]
    pos = word_with_pos[1]
    return pos

def lesk_witk_lemmatizer(tokens, specific_token, specific_token_pos):
    wnLemmatizer = WordNetLemmatizer()

    hmm_tagger = nltk.hmm.HiddenMarkovModelTrainer().train_supervised(brown.tagged_sents(categories="news")[:5000])
    
    # bring sentence or tokens?
    tagged_tokens = list(map(pos_according_to_tagger()))
    
    lemmatized_tokens = list(map(lambda w: wnLemmatizer.lemmatize(w), tokens))

    lemmatized_specific_token = wnLemmatizer.lemmatize(specific_token, specific_token_pos)
    return lesk(lemmatized_tokens, lemmatized_specific_token, specific_token)