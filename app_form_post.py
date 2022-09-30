'''
use html form using POST method
submit data and display it
'''

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=['GET','POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        context ={
            'name':name,
            'age':age
        }
        return render_template("display.html", data=context)
    return render_template("form.html")

@app.route("/display")
def display():
    return render_template("display.html")



if __name__=='__main__':
    app.run(debug=True, port=8080)
