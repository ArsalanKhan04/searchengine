import pickle
import sys


def get_parsed_set():
    with open("forwardindex/parsed_items/parsed.pkl", "rb") as f:
        currset = pickle.load(f)
    print("Current size of set: ", sys.getsizeof(currset), " bytes")
    return currset

def set_parsed_set(set):
    with open("forwardindex/parsed_items/parsed.pkl", "wb") as f:
        pickle.dump(set, f)