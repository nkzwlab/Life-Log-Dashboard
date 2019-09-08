#参考に過ぎないので、各自変えて大丈夫です。

from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def index():
    return 'This is the top page'

@app.route('/hello')
def hello_world():
    return 'And then here, you have more pages'

