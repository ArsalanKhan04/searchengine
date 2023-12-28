from wordlexicon.wordlexicon import get_wordID
from invertedindex.gettingWordLists import get_lists
from searching.ranking.rank import return_sorted_docs
from docdata.getdocdata.getjson import get_docdata, flush

# Going to complete this later:

def conv_query_wordids(querystring):
    words = querystring.split()
    wordID_list = [get_wordID(word) for word in words if get_wordID(word) > 179]
    return wordID_list

def get_wordelems(querystring):
    return get_lists(conv_query_wordids(querystring))

def return_common_docelems(arrays):
    if not arrays or any(not array for array in arrays):
        return []

    result = []
    pointers = [0] * len(arrays)

    while 1:

        # We will start by generating a vertical list so that we can find the minimum, this is done in O(h) time where h = no.of words
        
        current_list = [arrays[i][pointers[i]].doc_id if pointers[i] < len(arrays[i]) else 1000000 for i in range(len(arrays))]

        # We find the min, also done in O(h)
        min_val = min(current_list)

        if min_val >= 1000000:
            return result
        

        # Min indexes, found in O(h) as well
        min_indexes = [i for i in range(len(arrays)) if current_list[i]==min_val]

        # We relax the min indexes by appending their values to the results, also done in O(h)
        result.append([arrays[i][pointers[i]] for i in min_indexes])
        # We also increment all the min indexes
        for i in min_indexes:
            pointers[i] += 1

    return result


def get_response_json(sorted_docs):
    return [
        get_docdata(doc[1]) for doc in sorted_docs
    ]


def get_results(querystring):
    # Do something here
    all_wordelems = get_wordelems(querystring)
    common_docelems = return_common_docelems(all_wordelems)
    sorted_docs = return_sorted_docs(common_docelems)
    response = get_response_json(sorted_docs)
    return response
