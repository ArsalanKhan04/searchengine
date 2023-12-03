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

def parse(forward_index):
    # Modify this code accordingly
    invertedindex = invDS.InvertedIndex(len(lexicon_list))
    for eachdoc in forward_index.docelement:
        for eachwordelem in eachdoc:
            
    return invertedindex

