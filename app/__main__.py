#!/usr/bin/python
from bottle import route, request, run, template, static_file, get
import os
from settings import BASE_DIR
from search import search

@get('/static/<filepath:path>')
def g_static(filepath):
    return static_file(filepath, root=os.path.join(BASE_DIR, "statics"))

@route('/')
def r_index():
    return template(os.path.join(BASE_DIR, "templates/t_index.html"))

@route('/search')
def r_search():
    r = request.query.decode()
    print(r)
    string = r['s']
    dict_file = "dicts/cz_he.txt.json"
    result = search(dict_file, string)
    return template(os.path.join(BASE_DIR, "templates/t_search_result.html"), {'result': result})

@route('/xearch')
def r_xearch():
    r = request.query.decode()
    print(r)
    string = r['s']
    dict_file = "dicts/cz_he.txt.json"
    result = search(dict_file, string)
    return template(os.path.join(BASE_DIR, "templates/t_search_result_table.html"), {'result': result})



# main() runs run :D
def main(*args):
   run(host='localhost', port=8080)

#
#
# Runs main()
if __name__ == "__main__":
   main()
