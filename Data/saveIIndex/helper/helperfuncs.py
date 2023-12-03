import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(os.getcwd()))))
from Data.saveFIndex import forwardindex_file_pb2 as fpb

import Data.saveIIndex.invDS as invDS


def return_docelem(doc_id, word_element):

   
    
    docelem = invDS.DocElement()
    if docelem:
        docelem.word_id = word_element.word_id
        docelem.hits = word_element.hits
        docelem.title = word_element.title
        docelem.position.extend(word_element.position)
    return docelem 
    


if __name__ == '__main__':

    demo_wordelem = fpb.WordElement()
    demo_wordelem.word_id = 34
    demo_wordelem.hits = 50
    demo_wordelem.title = True
    demo_wordelem.position.extend([1, 3, 4, 5])

    print("helper functions running")

    demo_docelem = return_docelem(10, demo_wordelem)

