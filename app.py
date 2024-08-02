from flask import Flask, request
import requests
from bs4 import BeautifulSoup
import json
app = Flask(__name__)

def fetch(url, css_selector):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.content, "html.parser")
    name_arr = []
    for name in soup.select(css_selector):
        # name_arr.append(" ".join(name.text.split()))
        name_arr.append(name['href'])
    return name_arr

@app.route('/input_page', methods=['GET', 'POST'])
def input_page():
    html = "<form method='post' action='/input_page'>" \
        "<input type='text' name='url' style='width: 100%;' value='https://www.transfermarkt.com/fc-arsenal/startseite/verein/11' />" \
        "</br>" \
        "<input type='text' name='css_selector' style='width: 100%;' value='div.box div#yw1 table.items > tbody > tr > td.posrela > table.inline-table td.hauptlink > a' />" \
        "</br>" \
        "<button type='submit'>Submit</button></form>"
           
    if request.method == 'POST': 
        result = fetch(request.values['url'], request.values['css_selector'])
        return html + '<pre><code>' + json.dumps(result, indent=4) + '</code></pre>'

    return html

@app.route('/academy_player_now', methods=['GET', 'POST'])
def academy_player_now():
    html = "<form method='post' action='/input_page'>" \
        "<input type='text' name='url' style='width: 100%;' value='https://www.transfermarkt.com/fc-arsenal/startseite/verein/11' />" \
        "</br>" \
        "<input type='text' name='css_selector' style='width: 100%;' value='div.box div#yw1 table.items > tbody > tr > td.posrela > table.inline-table td.hauptlink > a' />" \
        "</br>" \
        "<button type='submit'>Submit</button></form>"
    
           
    if request.method == 'POST': 
        link_arr = fetch(request.values['url'], request.values['css_selector'])
        html += '<pre><code>' + json.dumps(link_arr, indent=4) + '</code></pre>'
        return html

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
    for name in soup.select('div.box div#yw1 table.items > tbody > tr > td.posrela > table.inline-table td.hauptlink > a'):
        name_arr.append(" ".join(name.text.split()))
    return name_arr
