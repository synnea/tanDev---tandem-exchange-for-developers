
import os
from flask import Flask, render_template, url_for, redirect, request
from flask_pymongo import PyMongo
from pymongo import MongoClient
from bson.objectid import ObjectId 

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'tandev'
app.config['MONGO_URI']= os.environ.get("MONGO_URI")

mongo = PyMongo(app)

client = MongoClient(app.config['MONGO_URI'])
db = client.tandev

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def home_page():

# Create a list of 6 random profiles to be used in the index.html carousel.


    carousel = db.profile.aggregate( [ { "$sample": { "size": 6 } } ])
    carousel = list(carousel)
    return render_template("pages/index.html", active="home", carousel=carousel)


@app.route('/about', methods=['GET'])
def about():
    return render_template("pages/about.html", active="about")

@app.route('/search', methods=['GET', 'POST'])
def search():
    return render_template("pages/search.html", active="search")

if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=(os.getenv('PORT')), debug="True")