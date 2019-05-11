from flask import Flask, render_template


app = Flask(__name__)

app.config.from_object('config')

@app.route('/')
def index():
    return render_template('index.html', data="A bot to answer all your questions")

if __name__ == "__main__":
    app.run()