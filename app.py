
import os
from flask import Flask, render_template, url_for, redirect, request, session, flash
from flask_pymongo import PyMongo
from werkzeug.security import check_password_hash, generate_password_hash
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'tandev'
app.config['MONGO_URI']= os.environ.get("MONGO_URI")

# Assign a randomized secret key
app.secret_key = os.urandom(24)

mongo = PyMongo(app)

client = MongoClient(app.config['MONGO_URI'])
db = client.tandev


# Begin creating routes
@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():

    """ Create a list of 6 random profiles whose display key is set to 'True' to be used in the index.html carousel. """


    carousel = db.profile.aggregate( [{ "$match" : { "display" : True } }, { "$sample": { "size": 6 } } ])
    carousel = list(carousel)
    return render_template("pages/index.html", active="index", carousel=carousel)



#About page
@app.route('/about', methods=['GET'])
def about():
    return render_template("pages/about.html", active="about")



# Search page
@app.route('/search', methods=['GET', 'POST'])
def search():
    return render_template("pages/search.html", active="search")


@app.route('/logreg', methods=['GET', 'POST'])
def logreg():
    return render_template("pages/logreg.html", active="logreg")


# Login
@app.route('/login', methods=['GET', 'POST'])
def login():

    """ Checks if the user already exists in the database """

    if request.method == 'POST' and request.form['btn'] == 'login':
        existing_user = db.profile.find_one({'username': request.form.get('username')})
        if not existing_user:
            flash("Hmm... this username doesn't seem to exist.")
            return redirect(url_for('login'))

        print('2nd thing works')
        if check_password_hash(existing_user["password"], 
        request.form.get("password")):
            session['username'] = request.form.get('username')
            return redirect(url_for('myprofile', username = session['username']))
        else:
            flash("Uh-oh! Password didn't match.")
            return redirect(url_for('login'))

    else:
        return render_template("pages/logreg.html", active="logreg")


# Register
@app.route('/register', methods=['GET', 'POST'])
def register():

    """ Check if the username already exists in the database. Return warning to the user if it exists.
    If it doesn't exist, add user to the database and create a new document in the database. """

    if request.method == 'POST' and request.form['btn'] == 'register':
        exists = db.profile.find_one({'username': request.form.get('username')})
        if exists:
            flash("Sorry, this username already exists")
            return redirect(url_for('register', _anchor = 'register-tab'))
        register = {
            "username": request.form.get('username'),
            "email": "",
            "password": generate_password_hash(request.form.get('password')),
            "imgUrl": "",
            "zipcode": "",
            "shortDescription": "",
            "description": "",
            "experience": "",
            "communicationStyle": {},
            "skills": {},
            "desiredSkills": {},
            "contact": {},
            "otherDetails": {},
            "published": datetime.now().strftime("%d-%M-%Y")
        }
        db.profile.insert_one(register)
        session['username'] = request.form.get('username')
        return redirect(url_for('myprofile', username = session['username']))

    return render_template("pages/logreg.html", active="logreg")


# My profile page
@app.route('/myprofile/<username>', methods = ['GET', 'POST'])
def myprofile(username):
    return render_template("pages/myprofile.html", username=username)


if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=(os.getenv('PORT')), debug="True")