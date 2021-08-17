import os
import json
from settings import BASE_DIR

print(BASE_DIR)

def search(string):
    
    dict_src = 'dicts/cz_he.json' 

    with open(dict_src, 'r') as file:
        dicty = json.load(file)
        for key, value in dicty.items():
            if key.startswith(string):
                item = {key: value}
                result.update(item)
                return result
