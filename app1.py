'''
Simple First Route created
'''
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return ("First Flask index route Call for Gohil")

@app.route("/db/<name>")
def db(name):
    return("My Name is: " + name)

if __name__=='__main__':
    app.run(debug=True, port=8080)
