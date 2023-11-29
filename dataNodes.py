'''
    DataNodes.py is a python file containing the structure definition of each data 
    element being used in our search engine.

'''

class DocElement():
    def __init__(self, doc_id, title, date, word_list, url):
        self.doc_id = doc_id
        self.title = title
        self.date = date
        self.word_list = word_list
        self.url = url
    

class WordElement():
    def __init__(self, word_id, hits, title):
        self.word_id = word_id
        self.hits = hits
        self.title = title



''''
    PARSING: going through the whole document



    makeElemList(wordlist):

        wordlist -> elemlist

        elemList = []       BASICALLY where your node will be stored one by one


        parsed_words = {}  BASICALLY THE DICTIONARY HAVING key, value pairs where key is word 
                            that has been parsed and value is the index where its node is stored
                            in elemList.

        for word in titleList:
            CHECK IF IT IS IN PARSED_WORDS.keys
            IF YES:
                GET ITS VALUE (INDEX)
                GO TO ELEMENT_LIST[INDEX]
                GET ITS HIT AND INCREMENT IT
            IF NOT:
                INITIALISE A NEW NODE
                word_id <-return_wordID(word)
                hits = 1
                title = 1

                DICTIONARY WORK
                - STORE NEW NODE INDEX IN DICTIONARY
                - key and value
                - key <- word
                - value <- length of element_list
                - parsed_words[key] = value

                APPEND NODE TO ELEMENT_LIST
                element_list.append(node)

        OLD IDEA:
            for word in wordlist:
                word_set.append(word)

                word_id <- return_wordID(word)
                hits = 1

        RETURN element_list


    parse(article):
        doc_id <- give urself (index)
        title <- title
        date <- date
        url <- url
        word_list ?

        WordElement? 

        word_list <- the function above




''''