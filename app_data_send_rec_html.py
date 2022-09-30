'''
call index.html
send data index.html
use 'url_for' and redirect onther route.
'''

from flask import Flask, redirect, render_template, url_for

app = Flask(__name__)

#simple index.html file call
@app.route("/")
def index():
    return render_template("index.html")

#Dyamic data send on template
@app.route("/gohil")
def gohil():
    surname = "Gohil"
    return render_template("index.html",data=surname)


#redirect onther route(page)
@app.route("/db")
def db():
    return redirect(url_for('gohil22'))

@app.route("/gohil11111111111111111111111111111111")
def gohil22():
    surname = "Gohil 11111111111111111111111111111111"
    return render_template("index.html",data=surname)


if __name__=='__main__':
    app.run(debug=True, port=8080)
