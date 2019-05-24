import os
from flask import Flask, request, url_for, send_from_directory
from werkzeug import secure_filename

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.getcwd()
app.config['PHOTO_FOLDER_B'] = 'photo/body'
app.config['PHOTO_FOLDER_C'] = 'photo/clothes'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


html = '''
    <!DOCTYPE html>
    <title>Upload File</title>
    <h1>Photo Upload</h1>
    <form method=post enctype=multipart/form-data>
         <input type=file name=file>
         <input type=submit value=upload>
	 <p>
	 {{form.user_id(size=80)}}
	 </p>
	 <p>{{form.(size=80)}}</p>
    </form>
    '''


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

    
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


@app.route('/bodypicture', methods=['GET', 'POST'])
def upload_file():
    print(request)
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],app.config['PHOTO_FOLDER_B'], filename))
        # save the id and path to the database

@app.route('/id')
def demo():
    if request.method == 'POST':
        

@app.route('/clothespicture', methods=['GET', 'POST'])
def upload_file():
    print(request)
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],app.config['PHOTO_FOLDER_C'], filename))
        # save the id and path to the database




if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80,debug=True)
