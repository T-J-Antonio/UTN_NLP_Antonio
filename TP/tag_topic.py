from get_tokens import tokens_from_file
import pyodbc
from numpy import log
from functools import reduce

def vocabulary(cursor):
    cursor.execute("SELECT word_proper FROM word")
    vocabulary = list(map(lambda row: (row.word_proper).rstrip(), cursor.fetchall()))
    return vocabulary

def prior_probability(cursor, topic_id):
    cursor.execute("SELECT COUNT(*) as topic_count FROM Text WHERE text_topic = " + str(topic_id))
    row = cursor.fetchone()
    topic_count = row.topic_count

    cursor.execute("SELECT COUNT(*) as total_count FROM Text")
    row = cursor.fetchone()
    total_count = row.total_count

    return topic_count / total_count

def total_word_count_from_topic(cursor, topic_id):
    cursor.execute("SELECT SUM(ocurrence_count) as total FROM Ocurrence WHERE ocurrence_topic = " + str(topic_id))
    row = cursor.fetchone()
    return row.total

def specific_word_count_from_topic(cursor, topic_id, word):
    cursor.execute("SELECT ocurrence_count as count FROM Ocurrence"
        + " JOIN Word on word_id = ocurrence_word"
        + " WHERE word_proper = \'" + word + "\' AND ocurrence_topic = " + str(topic_id))
    rows = cursor.fetchall()
    if len(rows) == 0: return 0
    else: return rows[0].count

def feature_likelihood(cursor, topic_id, token):
    total_word_count = total_word_count_from_topic(cursor, topic_id)
    specific_word_count = specific_word_count_from_topic(cursor, topic_id, token)
    v = vocabulary(cursor)
    return (specific_word_count + 1) / (total_word_count + len(v))

def topic_likelihood(cursor, topic_id, tokens):
    prior_p = prior_probability(cursor, topic_id)
    v = vocabulary(cursor)

    tokens_in_vocabulary = list(filter(lambda token: token in v, tokens))

    feature_likelihoods = list(map(lambda token: feature_likelihood(cursor, topic_id, token), tokens_in_vocabulary))

    log_feature_likelihoods = list(map(log, feature_likelihoods))

    return log(prior_p) + sum(log_feature_likelihoods)

def reduce1(function, a_list):
    return reduce(function, a_list[1:], a_list[0])

def max_by_snd(a_list):
    return reduce1(lambda tuple1, tuple2: tuple1 if tuple1[1] > tuple2[1] else tuple2, a_list)

def tag_topic(src):
    server = 'TOMIPC' 
    database = 'NLP_word_ocurrences'
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';TRUSTED_CONNECTION=yes')
    cursor = cnxn.cursor()

    cursor.execute("SELECT topic_id FROM Topic")
    topic_id_list = list(map(lambda row: row.topic_id, cursor.fetchall()))

    tokens = tokens_from_file(src)

    likelihoods = list(map(lambda topic_id: (topic_id, topic_likelihood(cursor, topic_id, tokens)), topic_id_list))

    max_likelihood = max_by_snd(likelihoods)

    best_match_id = max_likelihood[0]

    cursor.execute("SELECT topic_name FROM Topic WHERE topic_id = " + str(best_match_id))
    row = cursor.fetchone()
    best_match_name = row.topic_name
    return best_match_name
