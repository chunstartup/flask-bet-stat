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
    for name in soup.find_all("a", class_="hauptlink"):
        names_arr.append(name.decode_contents())
    return names_arr
