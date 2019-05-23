from flask import Flask, render_template, request, jsonify
from classes import Big_search
import os


app = Flask(__name__)

@app.route('/')
def index():    
    KEY =  os.environ.get('google_key')
    return render_template('index.html', KEY = KEY)


@app.route('/process', methods=['POST'])
def process():
    # here we address the key created in form.js json object in ajax
    result = request.form['answer']
    
    if result:
        new_big_search = Big_search(result) 
        return jsonify({'answer1' : new_big_search.search[0], 'answer2' : new_big_search.search[1], "map1" : new_big_search.search[2], "map2" : new_big_search.search[3]})

    return jsonify({'error' : "You didn't enter a question at all, please type something"})


if __name__ == "__main__":
    app.run()