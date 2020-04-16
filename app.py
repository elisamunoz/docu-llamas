import math
from forms import UpdateForm
from utils import find_categories, find_patterns, get_pattern, get_pattern_count
import os
from flask import Flask, render_template, redirect, url_for, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = "stitching"
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route('/')
@app.route('/home')
def get_home():
    """ 
    Homepage displays a set of Patterns and redirects to the main page
    """

    page = request.args.get('page', default=1, type=int)
    patterns_per_page = 6
    skip = (page - 1) * patterns_per_page

    all_categories = find_categories(mongo.db)
    total_patterns = get_pattern_count(mongo.db)
    total_pages = int(math.ceil(total_patterns / patterns_per_page))

    patterns = find_patterns(mongo.db).sort(
        "_id", -1).skip(skip).limit(patterns_per_page)
    return render_template(
        "home.html",
        patterns=patterns,
        total_pages=total_pages,
        current_page=page,
        categories=all_categories
    )


@app.route('/about')
def about():
    """
    About displays About section
    """
    page = request.args.get('about')
    return redirect(url_for('get_home', _anchor='about', page=page))


@app.route('/get_patterns')
def get_patterns():
    """
    get_patterns get patterns on Mongo DB and displays a set of Patterns
    """
    page = request.args.get('page')
    return redirect(url_for('get_home', _anchor='projects', page=page))


@app.route('/pattern/<pattern_id>')
def pattern(pattern_id):
    """
    Gets to a pattern in particular
    """
    try:
        the_pattern = get_pattern(mongo.db, pattern_id)
        all_categories = find_categories(mongo.db)
        return render_template('pattern.html', pattern=the_pattern, categories=all_categories)

    except Exception:
        return render_template('404.html')


@app.route('/add_pattern')
def add_pattern():
    """
    Form to add a new pattern 
    """
    form = UpdateForm(mongo.db)
    hasError = request.args.get('showError', default=False, type=bool)

    return render_template(
        'addpattern.html',
        form=form,
        isNew=True,
        hasError=hasError
    )


@app.route('/insert_pattern', methods=['POST'])
def insert_pattern():
    """
    Add a pattern to Mongo DB and displays it in the patterns section if sucessful
    """
    UpdateForm(mongo.db)
    UpdateForm(mongo.db, data=request.form.to_dict())

    form = UpdateForm(mongo.db, data=request.form.to_dict())
    is_valid: bool = form.validate()

    if is_valid:
        patterns = mongo.db.patterns
        patterns.insert_one(request.form.to_dict())
        return redirect(url_for('get_patterns'))
    else:
        return redirect(url_for('add_pattern', showError=True))


@app.route('/edit_pattern/<pattern_id>')
def edit_pattern(pattern_id):
    """
    Form to edit a pattern in particular
    """
    try:
        the_pattern = get_pattern(mongo.db, pattern_id)
        form = UpdateForm(mongo.db)

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

        return render_template(
            'addpattern.html',
            form=form,
            isNew=False,
            id=pattern_id
        )

    except Exception:
        return render_template('404.html')


@app.route('/update_pattern/<pattern_id>', methods=["POST"])
def update_pattern(pattern_id):
    """
   Updates a pattern on Mongo DB 
    """
    try:
        patterns = mongo.db.patterns
        patterns.update({'_id': ObjectId(pattern_id)},
                        {
            'category_name': request.form.get('category_name'),
            'pattern_name': request.form.get('pattern_name'),
            'pattern_by': request.form.get('pattern_by'),
            'pattern_yarn_weight': request.form.get('pattern_yarn_weight'),
            'pattern_gauge': request.form.get('pattern_gauge'),
            'pattern_needle_size': request.form.get('pattern_needle_size'),
            'pattern_yardage': request.form.get('pattern_yardage'),
            'pattern_size': request.form.get('pattern_size'),
            'pattern_language': request.form.get('pattern_language'),
            'pattern_url': request.form.get('pattern_url'),
            'pattern_notes': request.form.get('pattern_notes'),
            'pattern_img': request.form.get('pattern_img'),
            'pattern_difficulty': request.form.get('pattern_difficulty')
        })
        return pattern(pattern_id)
    except Exception:
        return render_template('404.html')


@app.route('/delete_pattern/<pattern_id>')
def delete_pattern(pattern_id):
    """
    Deletes a pattern in particular from Mongo DB
    """
    try:
        mongo.db.patterns.remove({'_id': ObjectId(pattern_id)})
        return redirect(url_for('get_patterns'))
    except Exception:
        return render_template('404.html')


if __name__ == '__main__':
    app.run(
        host=os.environ.get("IP") or '',
        port=int(os.environ.get("PORT") or 8080),
        debug=False
    )
