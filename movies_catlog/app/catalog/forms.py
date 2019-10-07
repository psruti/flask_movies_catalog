from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField
from wtforms.validators import DataRequired


class EditMovieForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    cast = StringField('Cast', validators=[DataRequired()])
    directors = StringField('Movie director', validators=[DataRequired()])
    submit = SubmitField('Update')


class CreateMovieForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    directors = StringField('Director', validators=[DataRequired()])
    avg_rating = FloatField('Rating', validators=[DataRequired()])
    cast = StringField('Cast', validators=[DataRequired()])
    img_url = StringField('Image', validators=[DataRequired()])
    prod_id = IntegerField('ProductionID', validators=[DataRequired()])
    submit = SubmitField('Create')