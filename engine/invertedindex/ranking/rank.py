from engine.invertedindex.invDS import DocElement


# def proximity_score()

# A function to calculate importance of documents
def return_rank(docelem_list):
    size = len(docelem_list)
    # making a new doc element which only contains doc_id and importance
    new_docelem = DocElement(docelem_list[0].doc_id, -1, 0, [], 0)
    # Calculate importance based on hits, title presence and size of doc_element list
    for docelem in docelem_list:
        new_docelem.importance += docelem.hits * 3 ** docelem.title + 10 ** size

    return new_docelem

if __name__ == '__main__':
    new_docelem1 = DocElement(1, 44, 0, [], 0)
    new_docelem2 = DocElement(1, 3, 0, [], 0)
    new_docelem3 = DocElement(1, 18, 1, [], 0)
    new_docelem4 = DocElement(1, 9, 1, [], 0)
    list = [new_docelem1, new_docelem2, new_docelem3, new_docelem4]
    print(return_rank(list))