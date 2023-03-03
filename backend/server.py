from flask import Flask, jsonify
from flask import request, g

from gamestop_scrapper import fetch_price

app = Flask(__name__)

@app.route('/gamestop', methods=['GET'])
def get_info():
    url = request.args.get('url')
    info = fetch_price(url)
    info_final = jsonify(info)
    info_final.headers.add('Access-Control-Allow-Origin', '*')
    return info_final

url_test = 'https://www.gamestop.com/video-games/playstation-5/products/nba-2k23---playstation-5/11206859-11206849.html?condition=Pre-Owned'

@app.route('/test', methods=['GET'])
def get_test():
    info = fetch_price(url_test)
    return info

if __name__ == "__main__":
    app.run(debug=True)