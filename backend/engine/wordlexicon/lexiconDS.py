class NewLexicon:
    def __init__(self):
        self.worddict = {}
        self.wordlist = []
        self.size = 0
    
    def get_wordID(self, word):
        return self.worddict[word]
    
    def get_word(self, index):
        return self.wordlist[index]
    
    def insert(self, word):
        self.wordlist.append(word)
        self.worddict[word] = self.size
        self.size+=1

    