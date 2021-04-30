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


# Example Code from Slides
# @app.route('/', methods=['GET', 'POST'])
# def function_name():
#     if request.method == 'GET':
#         #Code for GET here
#         return render_template('index.html')
#     elif request.method == 'POST':
#         #Code for POST here
#         # doc = {}
#         # for item in request.form:
#         #     doc[item] = request.form[item]
#         # mongo.db.users.insert_one(doc)
#         # return redirect('/login')
#         # user_info = {'Email': request.form['login-email'], 'Password': request.form['login-password']}
#         # found = mongo.db.users.find_one(user_info)

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


#Add a route for /login. 

#The GET method should render the "login.html" file

#The POST should take the user info and search the mongoDB database for that info (both provided in the slides and in the comments)

#Then, if something has been found, you want to redirect to "/home" as a GET method

#However, if nothing was found, then run this code: flash("The email/password doesn't work. Try again")

#After this, redirect to "/login" as a GET method

#All the information you need to fix the project can be found in the slides and other parts of the project given to you

#Feel free to ask any questions if you get stuck!

#Have fun!


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

