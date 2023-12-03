import Data.doc_data.doc_file_pb2 as dpb


# Making a function to parse an article to return a data_node
# to store document data separately which we will use later 
# to print search results

def parse(article):
    data_node = dpb.EachDocData()
    data_node.url = article['url']
    data_node.title = article['title']
    data_node.date = article['date']
    data_node.author = article['author']
    try:
        data_node.chars500 = article['content'][:500]
    except:
        data_node.chars500 = article['content']
    return data_node
