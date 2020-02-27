import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
  import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = "docu_meow"
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)

@app.route('/') 
def home():
    return render_template("home.html", docus=mongo.db.docus.find())

@app.route('/get_documentaries') # gets documentaries from MongoDB
def get_documentaries():
    return render_template("documentaries.html", docus=mongo.db.docus.find())

@app.route('/add_documentary')
def add_documentary():
    return render_template('adddocumentary.html')

# @app.route('/edit_documentary')
# def edit_documentary():
#     return render_template('editdocumentary.html')


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