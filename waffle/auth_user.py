from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField 
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from waffle.models import User

class Registration(FlaskForm):

    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=8)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=4, max=12)])
    confirm_password = PasswordField('Confirm Password', 
                                    validators=[DataRequired(), Length(min=4, max=12), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        print("validating username")
        user = User.query.filter_by(username=username.data).first()
        if user:
            print("user exists duh")
            raise ValidationError('Username already exists!')
    
    def validate_email(self, email):
        ("validating email")
        user = User.query.filter_by(email=email.data).first()
        if user:
            print("email exists duh")
            raise ValidationError('Email already exists!')

class LogIn(FlaskForm):

    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=4, max=12)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')



