'''main.py

Flask application to serve search engine logic

'''
import pickle 
import sys

from flask import (
    Flask,
    request,
    url_for,
    make_response,
    render_template,
    jsonify
)

from functions import look_for_words_beginning_with


app = Flask(__name__)

with open("resources/trie_obj", 'rb') as file:
    trie = pickle.load(file)

@app.route("/",  methods=['GET'])
def index():
    resp = make_response(render_template('index.html'), 200)
    return resp

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404

@app.route("/search/<term>")
def search_for_term(term):
    suggestions = look_for_words_beginning_with(trie, term)
    return jsonify(suggestions)
