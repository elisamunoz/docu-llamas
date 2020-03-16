from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired


class UpdateForm(FlaskForm):
    category = SelectField('Category', choices=[])
    language = StringField('Language', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    pattern_by = StringField('Project/Article by', validators=[DataRequired()])
    hook = StringField('Hook/Needle Size', validators=[DataRequired()])
    gauge = StringField('Gauge', validators=[DataRequired()])
    yarn_weight = StringField('Yarn weigth/Fabric type', validators=[DataRequired()])
    yardage = StringField('How much do you need?', validators=[DataRequired()])
    size = StringField('Project size', validators=[DataRequired()])
    difficulty = SelectField('Skill level', choices=[], default="")
    url = StringField('Project/Article url', validators=[DataRequired()])
    img = StringField('Project/Article image', validators=[DataRequired()])
    notes = TextAreaField('Note', validators=[DataRequired()])
    submit = SubmitField('Add Project')
