# Define Inverted Index
# Define Document Element
# Define importance function


'''
    Here is the Document Element, having the 5 main attributes
'''
class DocElement():
    def __init__(self, doc_id, hits, titlebool, position_list, importance):
        self.doc_id = doc_id
        self.hits = hits
        self.titlebool = titlebool
        self.position_list = position_list
        self.importance = importance

class InvertedIndex():
    def __init__(self, index_height):
        self.index_height = index_height
        self.wordelems = [[]] * index_height
    def bin_insert(self, docelem, word_id):
        
        list_ins = self.wordelems[word_id]
        # Will do a binary insertion over here inside the sorted list
        low = 0
        high = len(list_ins) - 1

        while low <= high:
            mid = (low + high) // 2

            if list_ins[mid].importance < docelem.importance:
                high = mid - 1
            else:
                low = mid + 1


        list_ins.insert(low, docelem)

        

def calculate_importance(hits, titlebool):
    return hits * (3 ^ titlebool)

if __name__ == '__main__':
    print(calculate_importance(21, False))