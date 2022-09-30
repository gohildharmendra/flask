'''
Jinja Templating
=> Jinja is the templating engine of python for its Web Application
=> The current version is jinja2
=> it is used to create HTML,XML & other markup language
=> it is used to rendaring data from controller function to the view.
=> by default intall when you install python Flask
=> Delimiters
    {%......%}-> for Statements
    {{......}}-> for printing output
    {#......#}-> for comments
    #.......##-> for Line statements
'''

from flask import Flask, make_response, Response, render_template, request, session

app = Flask(__name__)

@app.route("/")
def index():
    # skills =['Python','Django','DSA']
    skills ={
        '1':'Python',
        '2': 'DSA'
    }
    context ={
        'name':"Gohil DharmendraSinh",
        'place':"Una",
        'skills':skills
    }
    return render_template("jinja-html.html", data=context)


        
if __name__=='__main__':
    app.run(debug=True, port=8080)
