def makeElemList(titleList, wordList):
    elemList = []
    parsed_words = {}
    for word in titleList:
        if word in parsed_words.keys():
            index = parsed_words[word]      
            elemList[index][hits] += 1
        else: 
            word_node = WordElement(return_wordID(word), 1, 1)
            parsed_words[word] = len(elemList)
            elemList.append(word_node)
    for word in wordList:
        if word in parsed_words.keys():
            index = parsed_words[word]      
            elemList[index][hits] += 1
        else: 
            word_node = WordElement(return_wordID(word), 1, 0)
            parsed_words[word] = len(elemList)
            elemList.append(word_node)
    return elemList

def parse(article):
    doc_node = DocElement(article[id], article[title], article[date], makeElemList(article[titleList], article[wordList]),article[url])
    return doc_node