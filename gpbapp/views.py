from flask import Flask, render_template, request, jsonify
from classes import Big_search


app = Flask(__name__)

app.config.from_object('config')

@app.route('/')
def index():
    # if request.method == 'POST':        
    #     result_question = request.form.get('form_question')
    #     new_big_search = Big_search(result_question)   
    #     return render_template('index.html', res=new_big_search.search[1])
   
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    # here we address the key created in form.js json object in ajax
    result = request.form['answer']

    if result is not None:
        return jsonify({'answer' : result})

    return jsonify({'error' : "you didn't enter a question"})


if __name__ == "__main__":
    app.run()