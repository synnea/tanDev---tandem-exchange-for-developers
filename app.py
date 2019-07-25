
import os
from flask import Flask, render_template, url_for, redirect, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'tandev'
app.config['MONGO_URI']=os.environ.get("MONGO_URI")


@app.route('/')
def get_index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=(os.getenv('PORT')), debug="True")