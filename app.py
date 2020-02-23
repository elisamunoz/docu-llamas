import os
import pymongo
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
  import env 

app = Flask(__name__)

MONGO_URI = os.environ.get("MONGO_URI")

mongo = PyMongo(app)

@app.route('/') 

@app.route('/get_documentaries') 
def get_documentaries():
    return render_template("documentaries.html", docus=mongo.db.docus.find())


# if __name__ == '__main__':
#     app.run(host=os.environ.get("IP"),
#     port=int(os.environ.get("PORT")),
#     debug=True)
    
if __name__ == '__main__': #to run locally
    app.run(
        # host='http://127.0.0.1',
        port=8080,
        debug=True
    )