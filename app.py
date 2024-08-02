from flask import Flask
import requests
from bs4 import BeautifulSoup
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/scrape_squad')
def scrape_squad():
    print('hi')
    
    url = "https://www.transfermarkt.com/fc-arsenal/startseite/verein/11"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(url, headers=headers)

    # Debugging: Print response status code and text
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text[:100]}")  # Only print the first 100 characters
    
    soup = BeautifulSoup(response.content, "html.parser")
    name_arr = []
    for name in soup.find_all("ul", class_="data-header__items"):
        name_arr.append(name.text)
    return name_arr
