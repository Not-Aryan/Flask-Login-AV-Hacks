import flask
from flask import *
import flask_bootstrap
import flask_pymongo
from flask_bootstrap import Bootstrap
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask("Login-System")
app.config["MONGO_URI"] = "mongodb://127.0.0.1:27017/login-system-db"
app.config['SECRET_KEY'] = 'anything_here'

Bootstrap(app)
mongo = PyMongo(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        doc = {}
        for item in request.form:
            doc[item] = request.form[item]
        mongo.db.users.insert_one(doc)
        flash('Account created successfully!')
        return redirect('/login')


@app.route('/home')
def home():
    if 'user-info' in session:
        return render_template('home.html')
    else:
        flash("You need to login first!")
        return redirect('/login')

@app.route('/logout')
def logout():
    session.pop('user-info')
    return redirect('/login')

app.run(debug=True)

