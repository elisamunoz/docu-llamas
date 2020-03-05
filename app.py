import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
  import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = "stitching"
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)

@app.route('/') 

@app.route('/get_patterns') # get_patterns from MongoDB
def get_patterns():
    return render_template("home.html", patterns=mongo.db.patterns.find())

@app.route('/home') # gets patterns from MongoDB
def get_home():
    return render_template("home.html", patterns=mongo.db.patterns.find())

@app.route('/get_pattern/<pattern_id>')
def get_pattern(pattern_id):
    the_pattern = mongo.db.patterns.find_one({"_id": ObjectId(pattern_id)})

    all_categories = mongo.db.categories.find()
    return render_template('getpattern.html', pattern=the_pattern, categories=all_categories)

@app.route('/add_pattern')
def add_pattern():
    return render_template('addpattern.html', categories=mongo.db.categories.find())

@app.route('/insert_pattern', methods=['POST'])
def insert_pattern():
    patterns = mongo.db.patterns
    patterns.insert_one(request.form.to_dict())
    return redirect(url_for('get_patterns'))

@app.route('/edit_pattern/<pattern_id>')
def edit_pattern(pattern_id):
    the_pattern = mongo.db.patterns.find_one({"_id": ObjectId(pattern_id)})

    all_categories = mongo.db.categories.find()
    all_difficulty = mongo.db.difficulty.find()
    return render_template(
        'editpattern.html',
        pattern=the_pattern,
        categories=all_categories,
        difficulty=all_difficulty
    )

@app.route('/update_pattern/<pattern_id>', methods=["POST"])
def update_pattern(pattern_id):
    patterns = mongo.db.patterns
    patterns.update( {'_id': ObjectId(pattern_id)}, 
    {
        'category_name':request.form.get('category_name'),
        'pattern_name':request.form.get('pattern_name'),
        'pattern_by':request.form.get('pattern_by'),
        'pattern_yarn_weight': request.form.get('pattern_yarn_weight'),
        'pattern_gauge':request.form.get('pattern_gauge'),
        'pattern_needle_size':request.form.get('pattern_needle_size'),
        'pattern_yardage':request.form.get('pattern_yardage'),
        'pattern_size':request.form.get('pattern_size'),
        'pattern_language':request.form.get('pattern_language'),
        'pattern_url':request.form.get('pattern_url'),
        'pattern_notes':request.form.get('pattern_notes'),
        'pattern_img':request.form.get('pattern_img'),
        'pattern_difficulty':request.form.get('pattern_difficulty')
    })
    return get_pattern(pattern_id)

@app.route('/delete_pattern/<pattern_id>')
def delete_pattern(pattern_id):
    mongo.db.patterns.remove({'_id': ObjectId(pattern_id)})
    return redirect(url_for('get_patterns'))


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