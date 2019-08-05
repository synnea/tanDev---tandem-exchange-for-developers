
import os
from flask import Flask, render_template, url_for, redirect, request
from flask_pymongo import PyMongo
from pymongo import MongoClient
from bson.objectid import ObjectId 

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'tandev'
app.config['MONGO_URI']=os.environ.get("MONGO_URI")

mongo = PyMongo(app)

client = MongoClient(app.config['MONGO_URI'])
db = client.tandev

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def home_page():


    carousel = db.profile.aggregate( [ { "$sample": { "size": 2 } } ])
    carousel = list(carousel)
    return render_template("pages/index.html", active="home", carousel=carousel)

if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=(os.getenv('PORT')), debug="True")