#!/usr/bin/env python3

from flask import Flask, render_template, jsonify
import requests
from key import key

app = Flask(__name__)

search_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
details_url = "https://maps.googleapis.com/maps/api/place/details/json"


@app.route("/", methods=["GET"])
def retrieve():
    return render_template('layout.html')


@app.route("/sendRequest/<string:query>")
def results(query):
    url = "https://www.google.com"
    return jsonify({'result': url})


if __name__ == '__main__':
    app.run(debug=True)
