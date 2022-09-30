'''
PyMySql 1
pip install PyMySQL

'''

import pymysql
from flask import Flask

app = Flask(__name__)
ip='localhost'
username='admin'
password='admin@123'
db_name='flask_example'
cursorclass=pymysql.cursors.DictCursor

@app.route("/", methods=['GET','POST'])
def index():
    try:
        # db = pymysql.connect(ip, username, password, db_name,cursorclass)
        db = pymysql.connect(host=ip, user=username, password=password, database=db_name, cursorclass=cursorclass)
        cur = db.cursor()        
        return("database Exist")
    except Exception as e:        
        return("database Not Exist")
    


if __name__=='__main__':
    app.run(debug=True, port=8080)
