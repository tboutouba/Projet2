from flask import Flask, render_template, send_from_directory
from MVP1 import liste_candidats, data_test

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('Home.html')

@app.route('/Liste des candidats')
def liste_des_candidats():
   return render_template('liste des candidats.html',data = data_test)
   
@app.route('/candidat/<string:id>/')
def candidat(id):
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



if __name__=='__main__':
    app.run(debug=True)