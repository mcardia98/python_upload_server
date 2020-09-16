import os
from flask import Flask, request
from werkzeug.utils import secure_filename

# example curl command to upload file to server:
# curl -X POST -F file=@filename.ext http://IP:PORT/upload_file
save_folder = "/root/dump/"

app = Flask(__name__)
app.config["upload_folder"] = save_folder
@app.route("/upload_file", methods=['POST','PUT'])
def upload_file():
    file = request.files['file']
    filename=secure_filename(file.filename)   
    file.save(os.path.join(app.config['upload_folder'], filename))
    return "file saved\n"

if __name__=="__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
