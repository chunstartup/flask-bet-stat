from flask import Flask, request, render_template
import requests
from bs4 import BeautifulSoup
import json
app = Flask(__name__)


# Variable

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

premier_league_url = 'https://www.transfermarkt.com/premier-league/startseite/wettbewerb/GB1'


def bs_parse(response, css_selector, info_type):
    soup = BeautifulSoup(response.content, "html.parser")

    if info_type == 'html':
        return soup

    name_arr = []
    for name in soup.select(css_selector):
        if info_type == 'href':
            name_arr.append(name['href'])
        else:
            name_arr.append(name.text)
    return name_arr

def fetch(url):
    response = requests.get(url, headers=headers)

    return response

def fetch_parse(url, css_selector, info_type):
    response = fetch(url)
    name_arr = bs_parse(response, css_selector, info_type)

    return name_arr




@app.route('/', methods=['GET', 'POST'])
def root():
    return render_template('root.html')

@app.route('/academy_player_now', methods=['GET', 'POST'])
def academy_player_now():
    result_arr = []
    prefill_obj = {
        'url': 'https://www.transfermarkt.com/fc-arsenal/startseite/verein/11',
        'css_selector': 'div.box div#yw1 table.items > tbody > tr > td.posrela > table.inline-table td.hauptlink > a',
        'action': '/academy_player_now'
    }
    if request.method == 'POST': 
        result_arr = fetch_parse(request.values['url'], request.values['css_selector'], 'href')
    return render_template('try.html', prefill_obj=prefill_obj, result_arr=result_arr)

@app.route('/html', methods=['GET', 'POST'])
def html():
    result_arr = []
    prefill_obj = {
        'url': 'https://www.transfermarkt.com/fc-arsenal/startseite/verein/11',
        'css_selector': 'html',
        'action': '/html'
    }

    if request.method == 'POST': 
        result_arr = fetch_parse(request.values['url'], request.values['css_selector'], 'html')
    return render_template('try.html', prefill_obj=prefill_obj, result_arr=result_arr)