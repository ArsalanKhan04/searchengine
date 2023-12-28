'''
    In this file, we will be implementing functions to access the documents for each word ID

'''

from invertedindex import invDS

open_invertedindex = {}

def get_list(word_id):

    word_id_index = f"invindex{word_id//500}"

    if word_id_index not in open_invertedindex.keys():

        currInvIndex = invDS.load_from_binary_file(f"engine/invertedindex/data/{word_id_index}.bin")
        open_invertedindex[word_id_index] = currInvIndex

    else:

        currInvIndex = open_invertedindex[word_id_index]

    return currInvIndex.wordelems[word_id%500]

def get_lists(word_ids):
    return [get_list(word_id) for word_id in word_ids]


def flush():
    open_invertedindex={}