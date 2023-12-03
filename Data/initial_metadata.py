# We are importing system to get data from top directory
import sys, os
currpath = os.path.dirname(os.path.abspath(os.getcwd()))
print(currpath)
sys.path.append(currpath)

import metadata_pb2 as mpb
from wordlexicon import lexicon_list
metadata = mpb.MetaData()

with open("metadata.pb", "rb") as f:
    file_content = f.read()

metadata.ParseFromString(file_content)

metadata.lexiconheight = len(lexicon_list)
print(metadata.lexiconheight)

file_content = metadata.SerializeToString()


with open("metadata.pb", "wb") as f:
    f.write(file_content)