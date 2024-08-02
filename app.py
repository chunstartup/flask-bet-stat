from flask import Flask, request
import requests
from bs4 import BeautifulSoup
import json
app = Flask(__name__)

def fetch(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.content, "html.parser")
    name_arr = []
    tbody = soup.select_one('div.box div#yw1 table.items > tbody')
    for name in tbody.select('tr > td.posrela > table.inline-table td.hauptlink > a'):
        name_arr.append(" ".join(name.text.split()))
    return name_arr

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/input_page', methods=['GET', 'POST'])
def input_page():
    html = "<form method='post' action='/input_page'><input type='text' name='url' /><input type='text' name='css_selector' />" \
            "</br>" \
           "<button type='submit'>Submit</button></form>"
    print(f"Html: {html}")
           
    if request.method == 'POST': 
        result = fetch(request.values['url'])
        return html + '<pre><code>' + json.dumps(result) + '</code></pre>'

    return html

@app.route('/scrape_squad')
def scrape_squad():
    url = "https://www.transfermarkt.com/fc-arsenal/startseite/verein/11"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(url, headers=headers)
    
    soup = BeautifulSoup(response.content, "html.parser")
    name_arr = []
    tbody = soup.select_one('div.box div#yw1 table.items > tbody')
    for name in tbody.select('tr > td.posrela > table.inline-table td.hauptlink > a'):
        name_arr.append(" ".join(name.text.split()))
    return name_arr

@app.route('/scrape_squad2')
def scrape_squad2():
    url = "https://www.transfermarkt.com/fc-arsenal/startseite/verein/11"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(url, headers=headers)
    
    soup = BeautifulSoup(response.content, "html.parser")
    name_arr = []
    # tbody = soup.select_one('div.box div#yw1 table.items > tbody')
    for name in soup.select('div.box div#yw1 table.items > tbody > tr > td.posrela > table.inline-table td.hauptlink > a'):
        name_arr.append(" ".join(name.text.split()))
    return name_arr
