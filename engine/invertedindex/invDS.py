# Define Inverted Index
# Define Document Element
# Define importance function
import struct

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
        self.wordelems = [[] for _ in range (index_height)]
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

    def serialize_to_binary(self, filename):
        with open(filename, "wb") as file:

            file.write(struct.pack('I', self.index_height))

            for word_elem in self.wordelems:
                #Writing the number of docelement in a word_elem
                file.write(struct.pack("I", len(word_elem)))

                #Writing each docelement's attributes
                for doc_elem in word_elem:
                    file.write(struct.pack("I", doc_elem.doc_id))
                    file.write(struct.pack("I", doc_elem.hits))
                    file.write(struct.pack("?", doc_elem.titlebool))
                    file.write(struct.pack("I", len(doc_elem.position_list)))

                    for position in doc_elem.position_list:
                        file.write(struct.pack("I", position))
                    
                    file.write(struct.pack("I", doc_elem.importance))
    
def load_from_binary_file(filename):
    with open(filename, 'rb') as file:
        #Start by reading the index's height
        index_height = struct.unpack('I', file.read(4))[0]
        # Create a new InvertedIndex with the read index height
        inverted_index = InvertedIndex(index_height)

        # Read each list of DocElements
        for i in range(index_height):
            # Read the number of elements in the list
            num_elements = struct.unpack('I', file.read(4))[0]

            # Read each DocElement's attributes
            for _ in range(num_elements):
                doc_id = struct.unpack('I', file.read(4))[0]
                hits = struct.unpack('I', file.read(4))[0]
                titlebool = struct.unpack('?', file.read(1))[0]
                position_list_length = struct.unpack('I', file.read(4))[0]

                # Read each position in the position list
                position_list = [struct.unpack('I', file.read(4))[0] for _ in range(position_list_length)]

                importance = struct.unpack('I', file.read(4))[0]

                # Create a new DocElement and append it to the inverted index
                doc_element = DocElement(doc_id, hits, titlebool, position_list, importance)
                inverted_index.wordelems[i].append(doc_element)

    return inverted_index

        

def calculate_importance(hits, titlebool):
    return hits * (3 ** titlebool)

if __name__ == '__main__':
    print(calculate_importance(21, False))