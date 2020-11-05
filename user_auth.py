from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField 
from wtforms.validators import DataRequired, Length, Email, EqualTo

class Registration(FlaskForm):

    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=8)])
    email = StringField('Email', validators=[DataRequired(), Email()])

    password = PasswordField('Password', validators=[DataRequired(), Length(min=4, max=12)])
    confirm_password = PasswordField('Confirm Password', 
                                    validators=[DataRequired(), Length(min=4, max=12), EqualTo('password')])

    submit = SubmitField('Register')

class LogIn(FlaskForm):

    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired(), Length(min=4, max=12)])
    remember = BooleanField('remember me')
    submit = SubmitField('log in')



