# We need to implement get json in such a way that it stores the document datas before it flushes it

import docdata.protobufs.doc_file_pb2 as dpb
from metadata.metadatafuncs import get_metadata

open_docs = {}

lexiconheight, totaldocs, forwardindexlimit = get_metadata()

def get_docdata(doc_id):

    docdata_index = f"docdata_{int(doc_id//forwardindexlimit) + 1}"

    if docdata_index not in open_docs.keys():

        docdata = dpb.DocData()
        with open(f"engine/docdata/{docdata_index}.0.pb", "rb") as f:
            filecontent = f.read()
        docdata.ParseFromString(filecontent)

        open_docs[docdata_index] = docdata
    
    else:
        docdata = open_docs[docdata_index]

    eachdocdata = docdata.eachdoc[doc_id%forwardindexlimit]
    return {
        "url":eachdocdata.url,
        "title":eachdocdata.title,
        "date":eachdocdata.date,
        "chars500":eachdocdata.chars500,
        "author":eachdocdata.author
    }

def flush():
    open_docs = {}