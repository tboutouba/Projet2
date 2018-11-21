from flask import Flask, render_template
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
    return render_template('candidat.html',id=id, data=data_test)
    
    



if __name__=='__main__':
    app.run(debug=True)