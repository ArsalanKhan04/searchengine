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
