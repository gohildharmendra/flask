'''
WT Form
pip install flask-WTF

'''

from flask import Flask, url_for, request, render_template
from flask_wtf import Form
from wtforms import  TextAreaField, PasswordField, SubmitField
from wtforms import StringField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'db@test'

class UserForm(Form):
    username = StringField('Enter User name :')
    password = PasswordField('Enter Password :')
    submit = SubmitField("Submit")

@app.route('/', methods=['GET','POST'])
def index():
    form = UserForm()
    if request.method=='POST':
        return render_template('wtform-display.html')
    return render_template('wtform.html',form=form)






if __name__=='__main__':
    app.run(debug=True, port=8080)  
