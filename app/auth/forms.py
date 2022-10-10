from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField,
                     BooleanField, SubmitField,
                     ValidationError)
from wtforms.validators import DataRequired, Length, Email, EqualTo
from .. import db


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Length(1, 64), Email()],
                        render_kw={"placeholder": "user@email.com"})
    password = PasswordField('Password',
                             validators=[DataRequired()],
                             render_kw={"placeholder": "********"})
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = db.get_user(username.data)
        if user is not None:
            raise ValidationError('Username already in use.')

    def validate_email(self, email):
        user = db.get_user_by_email(email.data)
        if user is not None:
            raise ValidationError('Email already registered.')
