from flask import Flask, render_template, request


app = Flask(__name__)

app.config.from_object('config')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':        
        result_question = request.form.get('form_question')        
        return render_template('index.html', data="A bot to answer all your questions", res=result_question)
   
    return render_template('index.html', data="A bot to answer all your questions")

if __name__ == "__main__":
    app.run()