import sys
sys.path.append("../")
from wordlexicon.trie import Trie, TrieNode
import metadata.protobufs.metadata_pb2 as mpb
metadata = mpb.MetaData()

def get_metadata():
    with open("metadata/metadata.pb", "rb") as f:
        file_content = f.read()
    
    metadata.ParseFromString(file_content)
    return metadata.lexiconheight, metadata.totaldocs, metadata.forwardindexlimit

def save_metadata(lexiconheight, totaldocs, forwardindexlimit):
    metadata.lexiconheight = lexiconheight
    metadata.totaldocs = totaldocs
    metadata.forwardindexlimit = forwardindexlimit

    file_content = metadata.SerializeToString()


    with open("metadata/metadata.pb", "wb") as f:
        f.write(file_content)

