import os
import json
from hebrew_numbers import int_to_gematria
from bs4 import BeautifulSoup

def to_html(file_path):
    with open(file_path, 'w') as file_in:
        json_data = json.load(file_in)
        title = (json_data.get('heTitle'), json_data.get('title'))
        text = json_data.get('text')

        soup = BeautifulSoup(f"""<html>
    <head>
        <title>{title[1]}</title>
        <meta charset="utf-8" />
        <style></style>
    </head>
    <body><h1>{title[0]}</h1></body>
</html>""")

