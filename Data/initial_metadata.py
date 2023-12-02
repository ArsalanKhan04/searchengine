import metadata_pb2 as mpb

metadata = mpb.MetaData()
metadata.totaldocs = 0
metadata.forwardindexlimit = 1000

with open("metadata.pb", "wb") as f:
    f.write(metadata.SerializeToString())