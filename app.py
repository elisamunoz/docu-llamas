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

@app.route('/get_documentaries') # gets documentaries from MongoDB
def get_documentaries():
    return render_template("home.html", docus=mongo.db.docus.find())

@app.route('/home') # gets documentaries from MongoDB
def get_home():
    return render_template("home.html", docus=mongo.db.docus.find())

@app.route('/add_documentary')
def add_documentary():
    return render_template('adddocumentary.html', categories=mongo.db.categories.find())

@app.route('/insert_documentary', methods=['POST'])
def insert_documentary():
    docus = mongo.db.docus
    docus.insert_one(request.form.to_dict())
    return redirect(url_for('get_documentaries'))

@app.route('/edit_documentary/<documentary_id>')
def edit_documentary(documentary_id):
    the_documentary = mongo.db.docus.find_one({"_id": ObjectId(documentary_id)})

    all_categories = mongo.db.categories.find()
    return render_template('editdocumentary.html', documentary=the_documentary, categories=all_categories)

@app.route('/update_documentary/<documentary_id>', methods=["POST"])
def update_documentary(documentary_id):
    documentaries = mongo.db.docus
    documentaries.update( {'_id': ObjectId(documentary_id)}, 
    {
        'category_name':request.form.get('category_name'),
        'docu_title':request.form.get('docu_title'),
        'docu_summary':request.form.get('docu_summary'),
        'docu_url': request.form.get('docu_url'),
        'docu_lenght':request.form.get('docu_lenght'),
        'docu_produced_by':request.form.get('docu_produced_by'),
        'docu_language':request.form.get('docu_language'),
        'docu_img':request.form.get('docu_img')
    })
    return redirect(url_for('get_documentaries'))

@app.route('/delete_documentary/<documentary_id>')
def delete_documentary(documentary_id):
    mongo.db.docus.remove({'_id': ObjectId(documentary_id)})
    return redirect(url_for('get_documentaries'))


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