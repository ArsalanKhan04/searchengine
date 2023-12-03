'''
    Have to pass a forward index into the function

    Access every doc node in first loop
    In second loop, access word element
    Get docelem from muqaddas function
    pass it into an insertion function

    -> Parse    (forward_index)
    -> Insert  (word_id, docelem)
'''

# We are importing system to get data from top directory
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(os.getcwd()))))
from Data.saveFIndex import forwardindex_file_pb2 as fpb
import Data.saveIIndex.invDS as invDS
from wordlexicon import lexicon_list
from Data.saveIIndex.helper.helperfuncs import return_docelem


def parse(forward_index, invertedindex):
    # Modify this code accordingly
    for eachdoc in forward_index.docelement:
        for eachwordelem in eachdoc.wordelement:
            docelem = return_docelem(eachdoc.doc_id, eachwordelem)
            invertedindex.bin_insert(docelem, eachwordelem.word_id)
    return invertedindex

