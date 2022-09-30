'''
Documents Upload
'''

from traceback import print_tb
from flask import Flask,render_template, request, redirect
from werkzeug.utils import secure_filename
import os


app = Flask(__name__)
app.config['SECRET_KEY']="db@test"
app.config['UPLOAD_FOLDER']='/home/dharmendra/db-interview/flask/static/document/'
ALLOWED_EXTANSIONS = set(['pdf','png','.doc','jpg','jpeg'])

#Create File Upload
@app.route("/", methods=['GET','POST'])
def index():
    context ={'msg':"select Documents and click Upload Document"}
    if request.method=='POST':
        file = request.files['file']        
        if 'file' not in request.files:
            return redirect("/")
        elif file.filename =='':
            return("<script> alert('Please Select file') </script>")
        elif file:           
            file_name = secure_filename(file.filename)
            pathf = os.path.join(app.config['UPLOAD_FOLDER'])+file_name            
            file.save(pathf)            
            context ={'msg':"Documents Uploaded Successfully"}    
            return render_template("file-upload.html", data=context)
        else:
            return redirect(request.url)
    return render_template("file-upload.html", data=context)
        
if __name__=='__main__':
    app.run(debug=True, port=8080)
