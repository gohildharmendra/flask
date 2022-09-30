'''
cookies Created 
cookies Read 
cookies Deleted 
'''

from flask import Flask, make_response, request

app = Flask(__name__)

#create cookie
@app.route("/")
def index():
    cookie = make_response("Created Cookies")
    cookie.set_cookie('name',"Test NameDB", max_age=60*60)
    return(cookie)

#read cookie
@app.route("/read")
def read():
    if request.cookies.get('name'):
        cookie = make_response("Get Cookie Data name : {} ".format(request.cookies.get('name')))
    else:
        cookie = make_response("Created Cookies")
        cookie.set_cookie('name',"Test NameDB", max_age=60*60)
    return(cookie)

#delete cookies
@app.route("/delete")
def delete():
    cookie = make_response("Cookie Deleted successfully!")
    cookie.delete_cookie('name')
    return(cookie)
    
    
        
if __name__=='__main__':
    app.run(debug=True, port=8080)
