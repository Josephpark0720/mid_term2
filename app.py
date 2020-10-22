from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap, bootstrap_find_resource
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
bootstrap = Bootstrap(app)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'random'
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True)
    name = db.Column(db.String(80), unique=True)
    content = db.Column(db.String(300), unique=True)

    def __init__(self, title, name, content):
        self.title = title
        self.name = name
        self.content = content

    def __repr__(self):
        return "User<{}, {}, {}>".format(self.title, self.name, self.content)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return redirect(url_for('home'))
    else:
        return render_template('form.html')

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')