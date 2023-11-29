'''
    The following document contains the set of functions being used to create the forward index.

    In the forward indexing algorithm, a forward index will be created of the form:

    DOC_ELEMENT: WORD_ELEMENT, WORD_ELEMENT, WORD_ELEMENT
    DOC_ELEMENT: WORD_ELEMENT, WORD_ELEMENT, WORD_ELEMENT
    DOC_ELEMENT: WORD_ELEMENT, WORD_ELEMENT, WORD_ELEMENT

    Each DOC_ELEMENT and WORD_ELEMENT is defined in the dataNodes.py file

    We can use protocol buffers to store the data structure from this file

    We will divide each 1000 articles for 


'''

from dataNodes import DocElement, WordElement
from wordlexicon import return_wordID

def makeElemList(titleList, wordList):
    elemList = []
    parsed_words = {}
    for word in titleList:
        if word in parsed_words.keys():
            index = parsed_words[word]      
            elemList[index].hits += 1
        else: 
            word_node = WordElement(return_wordID(word), 1, 1)
            parsed_words[word] = len(elemList)
            elemList.append(word_node)
    for word in wordList:
        if word in parsed_words.keys():
            index = parsed_words[word]      
            elemList[index].hits += 1
        else: 
            word_node = WordElement(return_wordID(word), 1, 0)
            parsed_words[word] = len(elemList)
            elemList.append(word_node)
    return elemList

def parse(article, doc_id):
    titleList = article['title'].split()
    wordList = article['content'].split()
    doc_node = DocElement(doc_id, article['title'], article['date'], makeElemList(titleList, wordList),article['url'])
    return doc_node