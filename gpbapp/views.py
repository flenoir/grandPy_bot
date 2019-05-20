from flask import Flask, render_template, request, jsonify
from classes import Big_search


app = Flask(__name__)

app.config.from_object('config')

@app.route('/')
def index():
  
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    # here we address the key created in form.js json object in ajax
    result = request.form['answer']
    new_big_search = Big_search(result) 

    if result is not None:
        return jsonify({'answer1' : new_big_search.search[0], 'answer2' : new_big_search.search[1], "map" : new_big_search.search[2]})

    return jsonify({'error' : "you didn't enter a question"})


if __name__ == "__main__":
    app.run()