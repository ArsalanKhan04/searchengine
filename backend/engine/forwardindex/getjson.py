import os
import json

dir_path = r"forwardindex/JSONFILES/dir/"

def get_jsondata(filepath):
    with open(os.path.join(dir_path, filepath), "r") as f:
        json_data = json.load(f)
    print(len(json_data))
    return json_data