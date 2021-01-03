from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField, TextAreaField, validators
from wtforms.validators import DataRequired


class MusicLibrary(FlaskForm):
    title = StringField('Song Title', validators=[DataRequired()])
    band = StringField('Band Name', validators=[DataRequired()])
    genre = StringField('Music Type', validators=[DataRequired()])