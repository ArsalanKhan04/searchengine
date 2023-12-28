from invertedindex.invDS import DocElement
import heapq

def merge_sorted_arrays(arrays):
    result = []
    min_heap = []

    # Initialize the min heap with the first element from each array
    for i, array in enumerate(arrays):
        if array:  # Ensure the array is not empty
            heapq.heappush(min_heap, (array[0], i, 0))

    while min_heap:
        val, array_index, position = heapq.heappop(min_heap)
        result.append(val)

        # Move to the next position in the current array
        position += 1

        # If there are more elements in the current array, push the next one into the heap
        if position < len(arrays[array_index]):
            heapq.heappush(min_heap, (arrays[array_index][position], array_index, position))

    return result


# We will combining positions to calculate the proximity score
def proximity_score(positions):
    merged_pos = merge_sorted_arrays(positions)
    differences = []
    for i in range(1,len(merged_pos)):
        differences.append(merged_pos[i]-merged_pos[i-1])

    difference_score = (sum(differences)+1)/(len(differences) + 0.001)
    
    # print(merged_pos)
    # print(difference_score)
    return 50/difference_score 

# def proximity_score()

# A function to calculate importance of documents
def return_rank(docelem_list):
    size = len(docelem_list)
    # making a new doc element which only contains doc_id and importance
    doc_id = docelem_list[0].doc_id
    importance = 0
    # Calculate importance based on hits, title presence and size of doc_element list
    for docelem in docelem_list:
        importance += (docelem.hits * (3 ** docelem.titlebool))
    
    importance += 10**size
    importance += proximity_score([docelem.position_list for docelem in docelem_list])

    return -importance, doc_id 


def return_sorted_docs(list_of_docelemsarray):
    weighted_docs = [return_rank(docelem_list) for docelem_list in list_of_docelemsarray]
    heapq.heapify(weighted_docs)
    return [heapq.heappop(weighted_docs) for i in range(len(weighted_docs))]


if __name__ == '__main__':
    new_docelem1 = DocElement(1, 44, 0, [], 0)
    new_docelem2 = DocElement(1, 3, 0, [], 0)
    new_docelem3 = DocElement(1, 18, 1, [], 0)
    new_docelem4 = DocElement(1, 9, 1, [], 0)
    list = [new_docelem1, new_docelem2, new_docelem3, new_docelem4]
    print(return_rank(list))