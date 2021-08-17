#!/usr/bin/python
from bottle import route, request, run, template, static_file, get
import os
from settings import BASE_DIR
from search import search

@get('/static/<filepath>')
def g_static(filepath):
    return static_file(filepath, root=os.path.join(BASE_DIR, "statics"))

@route('/')
def r_index():
    return template(os.path.join(BASE_DIR, "templates/t_index.html"))

@route('/search')
def r_search():
    r = request.query.decode()
    print(r)
    string = r['string']
    dict_file = "dicts/cz_he.txt.json"
    result = search(dict_file, string)
    return result

# main() runs run :D
def main(*args):
   run(host='localhost', port=8080)

#
#
# Runs main()
if __name__ == "__main__":
   main()
