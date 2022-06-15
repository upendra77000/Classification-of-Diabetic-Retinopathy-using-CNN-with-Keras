import os
import flask as f
from flask import request
import model as ap
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads/' 
app = f.Flask(__name__, template_folder="static")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 

@app.route("/")
def index():
    return f.render_template("index.html")


@app.route("/about")
def about():
    return f.render_template("about.html")


@app.route("/results", methods=["POST", "GET"])
def upload():
    if request.method == 'POST':

        file=request.files["file"]
        filename = secure_filename(file.filename)
        path=os.path.join(app.config['UPLOAD_FOLDER'], filename)
        #if file not in 'UPLOAD_FOLDER':
        file.save(path)
        #os.remove(os.path.dirname(__file__) + '\static\output\graph.png') 
        result=ap.process_img(path,filename)
        return f.render_template("upload.html",image=result)

app.run(debug=True, port=8080, host="localhost")
