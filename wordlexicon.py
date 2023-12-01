'''
Wordlexicon.py contains the functions we will be using to interact with our lexicon.

In order to see how the lexicon was created,
please visit the notebooks in the lexicon folder


There are two main functions in this script,

We will use update lexicon function in order to update
the lexicon when we encounter new words.

We will use getwordID function simply to get the corresponding ID of each word
as defined by our lexicon

'''


# Importing and reading our lexicon
import lexicon.lexicon_proto_file_pb2 as lexproto
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

lexicon_pb_path = r"./lexicon/lexicon.pb"
lexicon = lexproto.Lexicon()

with open(lexicon_pb_path, 'rb') as file:
    protobufdata = file.read()
lexicon.ParseFromString(protobufdata)


# update function is pretty simple
def UpdateLexicon(lexicon):
    with open(lexicon_pb_path, 'wb') as f:
        f.write(lexicon.SerializeToString())    

# Making a list to simplify iteration
lexicon_list = list(lexicon.wordlist)

def return_wordID(word):
    
    try:
        word_id = lexicon_list.index(word)
        return word_id
    except ValueError:
        pass

    
    for pos in ['n', 'v', 'a', 'r']:
        lemmatized_word = lemmatizer.lemmatize(word, pos)
        try:
            word_id = lexicon_list.index(lemmatized_word)
            return word_id
        except ValueError:
            pass

    word_id = len(lexicon_list)
    lexicon_list.append(word)
    return word_id
