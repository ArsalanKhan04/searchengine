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
import pickle
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
from wordlexicon.lexiconDS import NewLexicon
import string

lexicon_path = "wordlexicon/lexicondict.pkl"


newLex = NewLexicon()
# Getting lexicon and saving its trie
with open(lexicon_path, "rb") as file:
    newLex = pickle.load(file)


def RemovePunctuation(word):
    return word.translate(str.maketrans('', '', string.punctuation))


def UpdateLexicon():
    with open(lexicon_path, "wb") as file:
        pickle.dump(newLex, file)

def GetLexiconSize():
    return newLex.size

def return_wordID(word):
    word = word.lower()
    word = "".join(char for char in word if char.isalpha())
    
    try:
        word_id = newLex.get_wordID(word)
    except KeyError:
        pass

    
    for pos in ['n', 'v', 'a', 'r']:
        lemmatized_word = lemmatizer.lemmatize(word, pos)
        try:
            word_id = newLex.get_wordID(lemmatized_word)
            return word_id
        except KeyError:
            pass

    word_id = newLex.size
    newLex.insert(word)
    return word_id

def return_word(index):
    return newLex.get_word(index)
