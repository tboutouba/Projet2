from flask import Flask, render_template
from data import Articles

app=Flask(__name__)

Articles=Articles()

@app.route('/')
def index():
    return render_template('Home.html')
    
@app.route('/About')
def about():
    return render_template('About.html')

@app.route('/Articles')
def articles():
    return render_template('articles.html', articles=Articles)

@app.route('/Article/<string:id>/')
def article(id):
    return render_template('article.html', id=id)

if __name__=='__main__':
    app.run(debug=True)