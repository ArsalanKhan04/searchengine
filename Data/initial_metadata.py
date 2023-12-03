import metadata_pb2 as mpb

metadata = mpb.MetaData()
metadata.totaldocs = 0
metadata.forwardindexlimit = 10000

file_content = metadata.SerializeToString()

with open("metadata.pb", "wb") as f:
    f.write(file_content)