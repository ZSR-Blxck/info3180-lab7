# Add any form classes for Flask-WTF here
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired


class LoginForm(FlaskForm):
    description = StringField('desc', validators=[InputRequired()])
    photo = FileField('Image', validators=[FileRequired(), FileAllowed(['jpg','png'], 'Please Upload Images Only!')])