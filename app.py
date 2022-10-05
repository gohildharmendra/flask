'''
API Create
Show all Display data endpoint [alldata]
Insert data endpoint [insert]
Delete data endpoint [delete]
One Record Diaply endpoint [/readone/<int:id>]

SQLAlchemy
pip install flask-sqlalchemy
python3 -m pip install PyMySQL[rsa]

##For Passwod
from urllib.parse import quote_plus
python3 -m pip install PyMySQL[rsa] #for password using with @ in password

'''


from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote_plus
import pymysql


app = Flask(__name__)
ip='localhost'
username='admin'
password= quote_plus("admin@123")
db_name='flask_example'

app.config['SQLALCHEMY_DATABASE_URI']=f'mysql+pymysql://{username}:{password}@{ip}/{db_name}'
app.config['SECRET_KEY']='db@test'
db = SQLAlchemy(app)

class APIUserModel(db.Model):
    __tablename__ = 'mysql_api_user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)    
    def __init__(self, username, email):
        self.username = username
        self.email = email
    def __repr__(self):
        return '<APIUserModel %r>' % self.username
    
    

@app.route('/',)
def index(): 
    return("Create API")

@app.route('/alldata', methods=['GET'])
def show_data():    
    data = APIUserModel.query.all()
    data_all =[]
    for item in data:
        data_all.append({"id":item.id, "name":item.username, "email":item.email})
    return jsonify(data_all)
    
@app.route('/insert', methods=['POST'])
def insert():
    name = request.get_json()['username']
    email = request.get_json()['email']
    api_user_model = APIUserModel(username = name, email = email)
    save_data = db.session
    try:
        save_data.add(api_user_model)
        save_data.commit()
    except:
        save_data.rollback()
        save_data.flush()
    id = api_user_model.id
    data = APIUserModel.query.filter_by(id = id).first()
    return jsonify({"id":data.id, "name":data.username,"email":data.email})

@app.route('/delete/<int:id>',methods=['DELETE'])
def delete(id):
    delete_data = db.session
    APIUserModel.query.filter_by(id =id).delete()
    delete_data.commit()
    # data = APIUserModel.query.all() 
    return show_data()    

@app.route('/readone/<int:id>')
def readone(id):
    try:    
        data = APIUserModel.query.filter_by(id = id).first()
        return jsonify({"id":data.id, "name":data.username,"email":data.email}) 
    except:
        return("Data Not Exist")
    
   
    
if __name__ == '__main__':
    with app.app_context():
        db.create_all()    
    app.run(debug=True, port=8080)