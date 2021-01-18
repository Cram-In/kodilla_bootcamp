from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField, TextAreaField, validators
from wtforms.validators import DataRequired


class TodoForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    description = StringField("Descryption", validators=[DataRequired()])
    status = BooleanField("I accept the task", [validators.DataRequired()])
