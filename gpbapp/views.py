from flask import Flask, render_template, request
from classes import Big_search


app = Flask(__name__)

app.config.from_object('config')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':        
        result_question = request.form.get('form_question')
        new_big_search = Big_search(result_question)   
        return render_template('index.html', res=new_big_search.search[1])
   
    return render_template('index.html')


if __name__ == "__main__":
    app.run()