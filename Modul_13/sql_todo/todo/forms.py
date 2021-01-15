from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField, TextAreaField, validators
from wtforms.validators import DataRequired


class TodoForm(FlaskForm):
    title = StringField("Task Title", validators=[DataRequired()])
    description = StringField("Task Description", validators=[DataRequired()])
