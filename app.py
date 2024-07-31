from flask import Flask
import requests
from bs4 import BeautifulSoup
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/scrape_squad')
def scrape_squad():
    url = "https://www.transfermarkt.com/fc-arsenal/startseite/verein/11"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    names_arr = []
    tbody = soup.select_one('div.box div#yw1 table.items > tbody')
    for name in tbody.select('tr > td.posrela > table.inline-table td.hauptlink > a'):
        names_arr.append(name.text)
    return names_arr
