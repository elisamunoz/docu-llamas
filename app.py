import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
  import env
from forms import UpdateForm


app = Flask(__name__)

app.config["MONGO_DBNAME"] = "stitching"
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config['SECRET_KEY'] =  os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

@app.route('/') 

@app.route('/get_patterns') # get_patterns from MongoDB
def get_patterns():
    all_categories = mongo.db.categories.find()
    return render_template("home.html", patterns=mongo.db.patterns.find(), categories=all_categories)

@app.route('/home') # gets patterns from MongoDB
def get_home():
    all_categories = mongo.db.categories.find()
    return render_template("home.html", patterns=mongo.db.patterns.find(), categories=all_categories)

@app.route('/get_pattern/<pattern_id>')
def get_pattern(pattern_id):
    try:
        the_pattern = mongo.db.patterns.find_one({"_id": ObjectId(pattern_id)})
        all_categories = mongo.db.categories.find()
        return render_template('getpattern.html', pattern=the_pattern, categories=all_categories)

    except Exception as e:
        return render_template('404.html')

def patternForm():
    all_categories = mongo.db.categories.find()
    all_difficulty = mongo.db.difficulty.find()

    form = UpdateForm()
    form.category_name.choices = [("", " ")] + [(cat['category_name'], cat['category_name']) for cat in all_categories]
    form.pattern_difficulty.choices = [("", " ")] + [(diff['pattern_difficulty'], diff['pattern_difficulty']) for diff in all_difficulty]

    return form

@app.route('/add_pattern')
def add_pattern():
    form = patternForm()

    return render_template('addpattern.html', form=form, isNew=True)

@app.route('/insert_pattern', methods=['POST'])
def insert_pattern():
    patterns = mongo.db.patterns
    patterns.insert_one(request.form.to_dict())
    return redirect(url_for('get_patterns'))

@app.route('/edit_pattern/<pattern_id>')
def edit_pattern(pattern_id):
    try:
        the_pattern = mongo.db.patterns.find_one({"_id": ObjectId(pattern_id)})
        form = patternForm()

        # Set default values
        form.category_name.default = the_pattern['category_name']
        form.pattern_language.default = the_pattern['pattern_language']
        form.pattern_name.default = the_pattern['pattern_name']
        form.pattern_by.default = the_pattern['pattern_by']
        form.pattern_needle_size.default = the_pattern['pattern_needle_size']
        form.pattern_gauge.default = the_pattern['pattern_gauge']
        form.pattern_yarn_weight.default = the_pattern['pattern_yarn_weight']
        form.pattern_yardage.default = the_pattern['pattern_yardage']
        form.pattern_size.default = the_pattern['pattern_size']
        form.pattern_difficulty.default = the_pattern['pattern_difficulty']
        form.pattern_url.default = the_pattern['pattern_url']
        form.pattern_img.default = the_pattern['pattern_img']
        form.pattern_notes.default = the_pattern['pattern_notes']
        form.process()

        return render_template('addpattern.html', form=form, isNew=False)

    except Exception as e:
        return render_template('404.html')
    # try:
    #     the_pattern = mongo.db.patterns.find_one({"_id": ObjectId(pattern_id)})

    #     all_categories = mongo.db.categories.find()
    #     all_difficulty = mongo.db.difficulty.find()
    #     return render_template(
    #         'editpattern.html',
    #         pattern=the_pattern,
    #         categories=all_categories,
    #         difficulty=all_difficulty
    #     )
    # except Exception as e:
    #     return render_template('404.html')
    

@app.route('/update_pattern/<pattern_id>', methods=["POST"])
def update_pattern(pattern_id):
    try:
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
    except Exception as e:
        return render_template('404.html')


@app.route('/delete_pattern/<pattern_id>')
def delete_pattern(pattern_id):
    try:
        mongo.db.patterns.remove({'_id': ObjectId(pattern_id)})
        return redirect(url_for('get_patterns'))
    except Exception as e:
        return render_template('404.html')


# if __name__ == '__main__':
#     app.run(host= ("IP"),
#     port=int(os.environ.get("PORT")),
#     debug=False)
    
if __name__ == '__main__': #to run locally
    app.run(
        # host='http://127.0.0.1',
        port=8080,
        debug=False
    )