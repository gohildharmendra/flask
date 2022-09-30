'''
Session Created 
Session Deleted
'''

from flask import Flask, session

app = Flask(__name__)
app.config['SECRET_KEY']='db@test'

#create session
@app.route("/")
def index():
    if 'hits' in session:
        session['hits'] = session.get('hits')+1
    else:
        session['hits']=1
    return("Total time site visites : {}".format(session.get('hits')))

#delete session
@app.route("/delete")
def delete():
    session.pop('hits',None)
    return("Session deleted successfully!!")
        
if __name__=='__main__':
    app.run(debug=True, port=8080)
