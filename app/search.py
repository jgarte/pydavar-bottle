import os
import json
from settings import BASE_DIR

print(BASE_DIR)

def search(dict_file, string):
    
    dict_path = os.path.join(BASE_DIR, dict_file)
    result = []

    with open(dict_path, 'r') as file:
        dicty = json.load(file)
        for item in dicty:
            
            if item[0].startswith(string):
                print(item)
                result.append(item)
    return result
