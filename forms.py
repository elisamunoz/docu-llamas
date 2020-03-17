from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired

class UpdateForm(FlaskForm):
    category_name = SelectField('Category', choices=[])
    pattern_language = StringField('Language', validators=[DataRequired()])
    pattern_name = StringField('Pattern/Article Name', validators=[DataRequired()])
    pattern_by = StringField('Pattern/Article by', validators=[DataRequired()])
    pattern_needle_size = StringField('Hook/Needle Size', validators=[DataRequired()])
    pattern_gauge = StringField('Gauge', validators=[DataRequired()])
    pattern_yarn_weight = StringField('Yarn weigth/Fabric type', validators=[DataRequired()])
    pattern_yardage = StringField('How much do you need?', validators=[DataRequired()])
    pattern_size = StringField('Available size', validators=[DataRequired()])
    pattern_difficulty = SelectField('Skill level', choices=[], default="")
    pattern_url = StringField('Pattern/Article url', validators=[DataRequired()])
    pattern_img = StringField('Pattern/Article image (url)', validators=[DataRequired()])
    pattern_notes = TextAreaField('Note', validators=[DataRequired()])
    submit = SubmitField('Add Pattern')
