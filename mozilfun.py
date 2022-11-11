from flask import Flask, send_from_directory
from requests import get
import bs4
import re

app = Flask(__name__)

homepage_html = open('html/home.html').read()
query_html_template = open('html/query.html').read()

@app.route('/')
def get_home():
    return homepage_html

@app.route('/html/<path:path>')
def send_report(path):
    return send_from_directory('html', path)

@app.route('/a/<addon>')  # type: ignore
def addon_page(addon:str):
    addon_page = get(f'https://addons.mozilla.org/en-US/firefox/addon/{addon}').text
    bs = bs4.BeautifulSoup(addon_page, features="html.parser")

@app.route('/s/<query>')  # type: ignore
def query_applets(query:str):
    search_page = get(f'https://addons.mozilla.org/en-US/firefox/search/?q={query}').text

    bs = bs4.BeautifulSoup(search_page, features="html.parser")
    entries = bs.findAll('div', {'class': "SearchResult-contents"})

    output_html = ''

    for entry in entries:
        link = entry.findAll('a', {'class':'SearchResult-link'})[0]
        link['href'] = re.sub(r'(https://addons.mozilla.org/en-US/firefox/addon)/([a-zA-Z0-9-_]+)/?(.*)',
         r'/a/\2', link['href'])
        link.string.replace_with('get addon')
        output_html += entry.prettify()
        output_html += link.prettify()

    output_final = query_html_template.replace('###', output_html)
    return output_final


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
