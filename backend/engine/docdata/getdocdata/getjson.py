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
    try:
        eachdocdata = docdata.eachdoc[doc_id%forwardindexlimit]
        return {
            "url":eachdocdata.url,
            "title":eachdocdata.title,
            "date":eachdocdata.date,
            "chars500":eachdocdata.chars500,
            "author":eachdocdata.author
        }
    except Exception:
        return {
            "url":"https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            "title":"This page is lost",
            "date":"I don't know date",
            "chars500":"This is a kind of easter egg i guess, this page is just not present in the docdata",
            "author":"Arsalan"
        }

def flush():
    global open_docs
    open_docs = {}