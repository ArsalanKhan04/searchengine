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
from wordlexicon.trie import Trie
import string

lexicon_triepath = "wordlexicon/lexiconTrie.pkl"


lexTrie = Trie()
# Getting lexicon and saving its trie
with open(lexicon_triepath, "rb") as file:
    lexTrie = pickle.load(file)


def RemovePunctuation(word):
    return word.translate(str.maketrans('', '', string.punctuation))


def UpdateLexicon():
    with open(lexicon_triepath, "wb") as file:
        pickle.dump(lexTrie, file)

def GetLexiconSize():
    return lexTrie.size

def return_wordID(word):
    
    word = word.lower()
    word = "".join(char for char in word if char.isalpha())

    try:
        word_id = lexTrie.get_index(word)
        if word_id == -1:
            raise ValueError
        return word_id
    except ValueError:
        pass

    
    for pos in ['n', 'v', 'a', 'r']:
        lemmatized_word = lemmatizer.lemmatize(word, pos)
        try:
            word_id = lexTrie.get_index(lemmatized_word)
            if word_id == -1:
                raise ValueError
            return word_id
        except ValueError:
            pass

    word_id = lexTrie.size
    lexTrie.insert(word, word_id)
    return word_id
