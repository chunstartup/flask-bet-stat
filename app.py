from flask import Flask
import requests
from bs4 import BeautifulSoup
app = Flask(__name__)

def fetch(url):
    print("fetch function")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.content, "html.parser")
    name_arr = []
    for name in soup.find_all("ul", class_="data-header__items"):
        name_arr.append(name.text)
    return name_arr

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/input_page', methods=['GET', 'POST'])
def input_page():
    html = "<form method='post' action='/input_page'><input type='text' name='url' />" \
            "</br>" \
           "<button type='submit'>Submit</button></form>"
    print(f"Html: {html}")
           
    if request.method == 'POST': 
        print(f"url: {request.values['url']}")
        result = fetch(request.values['url'])
        return html + '<textarea id="w3review" name="w3review" rows="4" cols="50">' + result + '</textarea>'

    return html

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
    tbody = soup.select_one('div.box div#yw1 table.items > tbody')
    for name in tbody.select('tr > td.posrela > table.inline-table td.hauptlink > a'):
        name_arr.append(name.text)
    return name_arr
