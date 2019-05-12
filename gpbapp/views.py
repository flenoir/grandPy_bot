from flask import Flask, render_template, request
from classes import Question, Big_search


app = Flask(__name__)

app.config.from_object('config')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':        
        result_question = request.form.get('form_question')
        new_big_search = Big_search(result_question)
        # new_question = Question(result_question)         
        return render_template('index.html', data="A bot to answer all your questions", res=new_big_search.search)
   
    return render_template('index.html', data="A bot to answer all your questions")

if __name__ == "__main__":
    app.run()