
#the following is just a sample, so erase it before you start writing your files
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello World"

if __name__ == "__main__":
  app.run()
