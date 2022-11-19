from nltk import pos_tag, word_tokenize
from nltk.wsd import lesk
from nltk.stem import WordNetLemmatizer

def get_or_else(x, y):
    return x if x is not None else y

def simplify_pos_tag(tag):
    tags = {
        "NOUN": "n",
        "ADJ": "a",
        "VERB": "v",
        "ADV": "r"
    }
    return get_or_else(tags.get(tag), "n")

def lesk_with_lemmatizer(tokens, specific_token, specific_token_pos):
    wnLemmatizer = WordNetLemmatizer()

    tagged_tokens = pos_tag(tokens, tagset = "universal")

    basically_tagged_tokens = list(map(lambda t: (t[0], simplify_pos_tag(t[1])), tagged_tokens))

    lemmatized_tokens = list(map(lambda t: wnLemmatizer.lemmatize(t[0], t[1]), basically_tagged_tokens))

    lemmatized_specific_token = wnLemmatizer.lemmatize(specific_token, specific_token_pos)

    return lesk(lemmatized_tokens, lemmatized_specific_token, specific_token_pos)

def match(sentence1, sentence2):
    tokens1 = word_tokenize(sentence1)
    tokens2 = word_tokenize(sentence2)
    synsets1 = set(map(lambda t: lesk_with_lemmatizer(tokens1, t, simplify_pos_tag(pos_tag([t])[0][1])), tokens1))
    synsets2 = set(map(lambda t: lesk_with_lemmatizer(tokens2, t, simplify_pos_tag(pos_tag([t])[0][1])), tokens2))
    
    synsets1 = set(filter(lambda s: s is not None, synsets1))
    synsets2 = set(filter(lambda s: s is not None, synsets2))

    return synsets1.intersection(synsets2)

coincidences = match("British websites ask for biscuits instead of cookies", "The British like to eat biscuits with their tea")
for s in coincidences: print(s.definition()) # Expected: definition of British and biscuit

coincidences = match("The candidate campaigned on the war on drugs", "The campaign proved to be unsuccessful")
for s in coincidences: print(s.definition()) # Expected: nothing (campaign as verb != campaign as noun)