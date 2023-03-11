from flask import Flask, jsonify
from flask import request, g
from flask_cors import CORS, cross_origin

from gamestop_scrapper import fetch_price

app = Flask(__name__)
CORS(app)

@app.route('/gamestop', methods=['GET'])
@cross_origin()
def get_info():
    url = request.args.get('url')
    info = fetch_price(url)
    info_final = jsonify(info)
    return info_final

# http://127.0.0.1:5000/test

@app.route('/test', methods=['GET'])
def hello():
    print('hello world')
    return 'hello world'


if __name__ == "__main__":
    app.run(debug=True)