from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired
from utils import find_categories, find_difficulty


class UpdateForm(FlaskForm):
    category_name = SelectField('Category', validators=[DataRequired()], choices=[])
    pattern_language = StringField('Language', validators=[DataRequired()])
    pattern_name = StringField('Pattern/Article Name', validators=[DataRequired()])
    pattern_by = StringField('Pattern/Article by', validators=[DataRequired()])
    pattern_needle_size = StringField('Hook/Needle Size')
    pattern_gauge = StringField('Gauge')
    pattern_yarn_weight = StringField('Yarn weigth/Fabric type')
    pattern_yardage = StringField('How much do you need?')
    pattern_size = StringField('Available size')
    pattern_difficulty = SelectField('Skill level', default="")
    pattern_url = StringField('Pattern/Article url', validators=[DataRequired()])
    pattern_img = StringField('Pattern/Article image (url)', validators=[DataRequired()])
    pattern_notes = TextAreaField('Note', validators=[DataRequired()])
    submit = SubmitField('Add Pattern')

    def __init__(self, db, *args, **kwargs):
        super(UpdateForm, self).__init__(*args, **kwargs)

        all_categories = find_categories(db)
        all_difficulty = find_difficulty(db)

        self.category_name.choices = [("", " ")] + [(cat['category_name'], cat['category_name']) for cat in all_categories]
        self.pattern_difficulty.choices = [("", " ")] + [(diff['pattern_difficulty'], diff['pattern_difficulty']) for diff
                                                         in all_difficulty]
