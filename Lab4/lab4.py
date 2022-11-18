from nltk import pos_tag, word_tokenize
from nltk.wsd import lesk
from nltk.stem import WordNetLemmatizer

def getOrElse(x, y):
    return x if x is not None else y

def simplify_pos_tag(tag):
    tags = {
        "NOUN": "n",
        "ADJ": "a",
        "VERB": "v",
        "ADV": "r"
    }
    return getOrElse(tags.get(tag), "n")

def lesk_witk_lemmatizer(tokens, specific_token, specific_token_pos):
    wnLemmatizer = WordNetLemmatizer()

    tagged_tokens = pos_tag(tokens, tagset = "universal")

    basically_tagged_tokens = list(map(lambda t: (t[0], simplify_pos_tag(t[1])), tagged_tokens))

    lemmatized_tokens = list(map(lambda t: wnLemmatizer.lemmatize(t[0], t[1]), basically_tagged_tokens))

    lemmatized_specific_token = wnLemmatizer.lemmatize(specific_token, specific_token_pos)

    return lesk(lemmatized_tokens, lemmatized_specific_token, specific_token_pos)

sentence = "I sat by the river bank watching the fish swim."
tokens = word_tokenize(sentence)
synset = lesk_witk_lemmatizer(tokens, "bank", "n")
print(synset.definition())