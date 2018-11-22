import os
from flask import Flask, render_template, send_from_directory,flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from MVP1 import liste_candidats, data_test


UPLOAD_FOLDER = '/Users/mac/Desktop/centrale/1ereannee/CodingWeeks/ProjetDoctolib/MVP1/fichiers'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app=Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('Home.html')

@app.route('/Liste des candidats')
def liste_des_candidats():
   return render_template('liste des candidats.html',data = data_test)
   
@app.route('/candidat/<string:id>/',methods=['GET', 'POST'])
def candidat(id):
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            print(1)
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            print(2)
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print(3)
            return redirect(request.url)
    Candidat=data_test[int(id)-1]
    return render_template('candidat.html',id = id,candidat=Candidat)

@app.route('/candidat/<string:id>/<string:fichier>')
def fichier(id,fichier):
    Candidat=data_test[int(id)-1]
    Fichier={}
    for element in Candidat["fichiers"]:
        if str(element["id"])==fichier:
            Fichier=element
            break
    return render_template('fichier.html',fichier=Fichier, id= id,candidat=Candidat)

@app.route('/fichiers/<string:fichier>')
def ouvrir_fichier(fichier):
    nom_fichier = fichier + ".pdf"
    return send_from_directory('/Users/mac/Desktop/centrale/1ereannee/CodingWeeks/ProjetDoctolib/MVP1/fichiers', nom_fichier)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

'''@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return 
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''


if __name__=='__main__':
    app.secret_key = 'some secret key'
    app.run(debug=True)