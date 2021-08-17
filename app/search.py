import os
import json
from settings import BASE_DIR

print(BASE_DIR)

def search(dict_file, string):
    
    dict_path = os.path.join(BASE_DIR, dict_file)
    result = {}

    with open(dict_path, 'r') as file:
        dicty = json.load(file)
        for key, value in dicty.items():
            if key.startswith(string):
                item = {key: value}
                result.update(item)
    return result
