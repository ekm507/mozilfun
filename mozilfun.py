from flask import Flask
from requests import get
import bs4

app = Flask(__name__)

homepage_html = open('html/home.html').read()
query_html_template = open('html/query.html').read()

@app.route('/')
def get_home():
    return homepage_html

@app.route('/s/<query>')  # type: ignore
def query_applets(query:str):
    search_page = get(f'https://addons.mozilla.org/en-US/firefox/search/?q={query}').text
    bs = bs4.BeautifulSoup(search_page, features="html.parser")
    entries = bs.findAll('div', {'class': "SearchResult-contents"})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
