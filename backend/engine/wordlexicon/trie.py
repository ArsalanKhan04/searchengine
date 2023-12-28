class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.index = -1

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.size = 0

    def insert(self, word, index):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        node.index=index
        self.size+=1

    def get_index(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return -1
            node = node.children[char]
        return node.index
    
    def _get_words_recursive(self, node, current_word, result):
        if node.is_end_of_word:
            result.append((current_word, node.index))

        for char, child_node in node.children.items():
            self._get_words_recursive(child_node, current_word + char, result)

    def get_all_words(self):
        result = []
        self._get_words_recursive(self.root, '', result)
        return result
