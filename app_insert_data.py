'''
PyMySql 2
pip install PyMySQL
Insert Data into Table
'''

import pymysql
from flask import Flask, render_template, request

app = Flask(__name__)
ip='localhost'
username='admin'
password='admin@123'
db_name='flask_example'
cursorclass=pymysql.cursors.DictCursor

@app.route("/", methods=['GET','POST'])
def index():
    if request.method=='POST':    
        try:
            # db = pymysql.connect(ip, username, password, db_name,cursorclass)
            db = pymysql.connect(host=ip, user=username, password=password, database=db_name, cursorclass=cursorclass)
            cur = db.cursor()        
            name = request.form['name']      
            city = request.form['city']
            sql = f"INSERT INTO user(name,city) VALUES('{name}','{city}')"
            print(sql)
            cur.execute(sql)
            db.commit()
            db.close()
            return("data Inserted Successfully")
        except Exception as e:        
            return("database Not Exist")
    return render_template('index.html')


if __name__=='__main__':
    app.run(debug=True, port=8080)
