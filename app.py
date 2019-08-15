
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
app.secret_key = os.urandom(24)

mongo = PyMongo(app)

client = MongoClient(app.config['MONGO_URI'])
db = client.tandev

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():

# Create a list of 6 random profiles to be used in the index.html carousel.


    carousel = db.profile.aggregate( [ { "$sample": { "size": 6 } } ])
    carousel = list(carousel)
    return render_template("pages/index.html", active="index", carousel=carousel)


@app.route('/about', methods=['GET'])
def about():
    return render_template("pages/about.html", active="about")


@app.route('/search', methods=['GET', 'POST'])
def search():
    return render_template("pages/search.html", active="search")


@app.route('/logreg', methods=['GET', 'POST'])
def logreg():
    return render_template("pages/logreg.html", active="logreg")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
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
        return redirect(url_for('account', username = session['username']))

    return render_template("pages/logreg.html", active="logreg")

@app.route('/account/<username>', methods = ['GET', 'POST'])
def account(username):
    return render_template("pages/account.html", username=username)


if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=(os.getenv('PORT')), debug="True")