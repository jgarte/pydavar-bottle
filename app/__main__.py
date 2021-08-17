#!/usr/bin/python
from bottle import route, run, template, static_file, get
import os
from settings import BASE_DIR


@get('/static/<filepath>')
def g_static(filepath):
    return static_file(filepath, root=os.path.join(BASE_DIR, "statics"))

@route('/index')
def r_index():
    pass

@route('/search/<string>')
def r_search(string):
    pass

# main() runs run :D
def main(*args):
   run(host='localhost', port=8080)

#
#
# Runs main()
if __name__ == "__main__":
   main()
