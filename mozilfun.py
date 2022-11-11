from flask import Flask

app = Flask(__name__)

homepage_html = open('html/home.html').read()
query_html_template = open('html/query.html').read()

@app.route('/')
def get_home():
    return homepage_html

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
