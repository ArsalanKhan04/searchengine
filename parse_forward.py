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

# from dataNodes import DocElement, WordElement # Before, dataNodes were used, but now proto data will be used so it is easily stored

import Data.saveFIndex.forwardindex_file_pb2 as fpb
from wordlexicon import return_wordID, lexicon_list

def makeElemList(titleList, wordList):
    elemList = []
    parsed_words = {}
    position = 0
    for word in titleList:
        if word in parsed_words.keys():
            index = parsed_words[word]      
            elemList[index].hits += 1
            elemList[index].position.append(position)
        else: 
            # WordElement(return_wordID(word), 1, 1)
            word_node = fpb.WordElement()
            word_node.word_id = return_wordID(word)
            word_node.hits = 1
            word_node.title = True
            word_node.position.append(position)
            parsed_words[word] = len(elemList)
            elemList.append(word_node)
        position+=1
    for word in wordList:
        if word in parsed_words.keys():
            index = parsed_words[word]      
            elemList[index].hits += 1
            elemList[index].position.append(position)
        else: 
            word_node = fpb.WordElement()
            word_node.word_id = return_wordID(word)
            word_node.hits = 1
            word_node.title = False
            word_node.position.append(position)
            parsed_words[word] = len(elemList)
            elemList.append(word_node)
        position+=1
    return elemList

def parse(article, doc_id):
    titleList = article['title'].split()
    wordList = article['content'].split()
    doc_node = fpb.DocElement()
    doc_node.doc_id = doc_id
    doc_node.wordelement.extend(makeElemList(titleList, wordList))
    return doc_node


'''
    We will now be making additional functions that make forward indexes based on barrels
'''

#   I have decided not to make barrels for now as i believe my code will perform better for only invIndex Barrels
#   Barrels for forward_index would be of a different type

'''
def makeElemList_barrel(titleList, wordList, barrel_size, barrel_index):


def parse_into_barrels(article, doc_id, barrel_size):
    total_words = len(lexicon_list)
    no_of_barrels = (total_words // barrel_size) + 1
    doc_nodes = [fpb.DocElement()] * no_of_barrels
    for doc_node in doc_nodes:
        titleList = article['title'].split()
        wordList = article['content'].split()
        doc_node = fpb.DocElement()
        doc_node.doc_id = doc_id
        doc_node.title = article['title']
        doc_node.date = article['date']
        doc_node.wordelement.extend(makeElemList(titleList, wordList))
        doc_node.url = article['url']
    return doc_nodes


'''