from flask import Flask, request, render_template
import requests
from bs4 import BeautifulSoup
import json
app = Flask(__name__)

def fetch(url, css_selector, info_type):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.content, "html.parser")
    name_arr = []
    for name in soup.select(css_selector):
        if info_type == 'href':
            name_arr.append(name['href'])
        else:
            name_arr.append(name.text)
    return name_arr

def getHtml(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.content, "html.parser")
    return soup

@app.route('/', methods=['GET', 'POST'])
def root():
    return render_template('root.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
    result_arr = []
    prefill_obj = {
        'url': 'https://www.transfermarkt.com/fc-arsenal/startseite/verein/11',
        'css_selector': 'div.box div#yw1 table.items > tbody > tr > td.posrela > table.inline-table td.hauptlink > a',
        'action': '/'
    }
    if request.method == 'POST': 
        result_arr = fetch(request.values['url'], request.values['css_selector'], 'href')
    return render_template('try.html', prefill_obj=prefill_obj, result_arr=result_arr)

@app.route('/academy_player_now', methods=['GET', 'POST'])
def academy_player_now():
    result_arr = []
    prefill_obj = {
        'url': 'https://www.transfermarkt.com/fc-arsenal/startseite/verein/11',
        'css_selector': 'div.box div#yw1 table.items > tbody > tr > td.posrela > table.inline-table td.hauptlink > a',
        'action': '/academy_player_now'
    }
    if request.method == 'POST': 
        result_arr = fetch(request.values['url'], request.values['css_selector'], 'href')
    return render_template('try.html', prefill_obj=prefill_obj, result_arr=result_arr)

@app.route('/bet', methods=['GET', 'POST'])
def bet():
    result_arr = []
    prefill_obj = {
        'url': 'https://bet.hkjc.com/football/odds/tournament.aspx?lang=ch&tournid=50030726&tmatchid=50030726',
        'css_selector': '#dContainer #dTourn div.betTypeAllOdds div.allSelections span.oddsLink > span.oddsVal',
        'action': '/bet'
    }

    if request.method == 'POST': 
        result_arr = fetch(request.values['url'], request.values['css_selector'], 'text')
    return render_template('try.html', prefill_obj=prefill_obj, result_arr=result_arr)

@app.route('/html', methods=['GET', 'POST'])
def html():
    result_arr = []
    prefill_obj = {
        'url': 'https://bet.hkjc.com/football/odds/tournament.aspx?lang=ch&tournid=50030726&tmatchid=50030726',
        'css_selector': 'html',
        'action': '/html'
    }

    if request.method == 'POST': 
        result_arr = getHtml(request.values['url'])
    return render_template('try.html', prefill_obj=prefill_obj, result_arr=result_arr)

@app.route('/league_england', methods=['GET', 'POST'])
def league_england():
    url = 'https://bet.hkjc.com/football/getJSON.aspx?jsontype=tournament.aspx&tournid=50030726'

    response = requests.post(url)

    return response.json()