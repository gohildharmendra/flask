'''
Create Table using SQLAlchemy

pip install flask-sqlalchemy
python3 -m pip install PyMySQL[rsa]

##For Passwod
from urllib.parse import quote_plus
python3 -m pip install PyMySQL[rsa] #for password using with @ in password

'''

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote_plus
import pymysql


app = Flask(__name__)
ip='localhost'
username='admin'
password= quote_plus("admin@123")
db_name='flask_example'

app.config['SQLALCHEMY_DATABASE_URI']=f'mysql+pymysql://admin:{password}@localhost/flask_example'
app.config['SECRET_KEY']='db@test'
db = SQLAlchemy(app)

class db_api_user(db.Model):
    # __tablename__ = 'db_api_user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)    
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<db_api_user %r>' % self.username
    
    

@app.route('/')
def index():
    return("Table Created App")

if __name__ == '__main__':
    with app.app_context():
        db.create_all()    
    app.run(debug=True, port=8080)