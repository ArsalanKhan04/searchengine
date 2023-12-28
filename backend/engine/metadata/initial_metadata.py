# We are importing system to get data from top directory
import sys
sys.path.append("../")
import os
print(os.getcwd())
from wordlexicon.trie import Trie, TrieNode
from wordlexicon.wordlexicon import GetLexiconSize
import protobufs.metadata_pb2 as mpb
metadata = mpb.MetaData()

# with open("metadata.pb", "rb") as f:
#     file_content = f.read()

# metadata.ParseFromString(file_content)

checkingTrie = Trie()
metadata.lexiconheight = GetLexiconSize()
metadata.totaldocs = 0
metadata.forwardindexlimit = 5000

file_content = metadata.SerializeToString()


with open("metadata.pb", "wb") as f:
    f.write(file_content)