import pyodbc
from get_tokens import tokens_from_file

server = 'TOMIPC' 
database = 'NLP_word_ocurrences'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';TRUSTED_CONNECTION=yes')
cursor = cnxn.cursor()

def already_in_ocurrence_table(token, topic_id):
    cursor.execute("SELECT ocurrence_word FROM Ocurrence"
        + " JOIN Word ON ocurrence_word = word_id"
        + " WHERE ocurrence_topic = " + str(topic_id) + " AND word_proper = \'" + token + "\'")
    rows = cursor.fetchall()
    if len(rows) > 0: return rows[0].ocurrence_word
    else: return -1

def already_in_another_topic(token):
    cursor.execute("SELECT ocurrence_word FROM Ocurrence"
        + " JOIN Word ON ocurrence_word = word_id"
        + " WHERE word_proper = \'" + token + "\'")
    rows = cursor.fetchall()
    if len(rows) > 0: return rows[0].ocurrence_word
    else: return -1

cursor.execute("SELECT text_path, text_topic FROM Text") 
rows = cursor.fetchall()
for row in rows:
    topic_id = row.text_topic
    path = (row.text_path).strip()
    print("Processing file: " + path)
    tokens = tokens_from_file(path)
    for token in tokens:
        token_id = already_in_ocurrence_table(token, topic_id)
        if token_id != -1:

            # Case 1: the word has already appeared in another text with this topic.
            cursor.execute("SELECT ocurrence_count FROM Ocurrence"
                    + " WHERE ocurrence_topic = " + str(topic_id) + " AND ocurrence_word = " + str(token_id))
            row = cursor.fetchone()
            new_value = row.ocurrence_count + 1
            cursor.execute("UPDATE Ocurrence SET ocurrence_count = " + str(new_value)
                + " WHERE ocurrence_topic = " + str(topic_id) + " AND ocurrence_word = " + str(token_id))
            cnxn.commit()
            print("Added 1 to counter corresponding to word: " + token + " with topic: " + str(topic_id))

        else:
            token_id = already_in_another_topic(token)
            if token_id != -1:
                
                # Case 2: the word has already appeared in another text, but not with this topic.
                cursor.execute("INSERT Ocurrence (ocurrence_topic, ocurrence_word, ocurrence_count)"
                    + " VALUES (" + str(topic_id) + ", " + str(token_id) + ", " + "1)")
                cnxn.commit()
                print("Inserted already existing word: " + token + " with topic: " + str(topic_id))


            else:

                # Case 3: the word has never yet appeared.
                cursor.execute("INSERT Word (word_proper) VALUES (\'" + token + "\')")
                cnxn.commit()
                cursor.execute("SELECT word_id FROM Word WHERE word_proper = \'" + token + "\'")
                row = cursor.fetchone()
                token_id = row.word_id
                cursor.execute("INSERT Ocurrence (ocurrence_topic, ocurrence_word, ocurrence_count)"
                    + " VALUES (" + str(topic_id) + ", " + str(token_id) + ", " + "1)")
                cnxn.commit()
                print("Inserted new word: " + token + " with topic: " + str(topic_id))

cnxn.close()