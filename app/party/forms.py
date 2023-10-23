from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, FloatField
from wtforms.validators import ValidationError, DataRequired, Length, Email

from app.models import User


class PartyForm(FlaskForm):
    label = TextAreaField('Название', validators=[
        DataRequired(), Length(min=1, max=140)])
    about = TextAreaField('О вечеринке', validators=[Length(min=1, max=140)])
    address = TextAreaField('Адрес', validators=[Length(min=1, max=140)])
    submit = SubmitField('Submit')
