from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField , TextAreaField
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

class Login(FlaskForm):

    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=4, max=12)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class UpdateAccount(FlaskForm):

    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=8)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Update')

    def validate_username(self, username):
        print("validating username")
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                print("user exists duh")
                raise ValidationError('Username already exists!')
    
    def validate_email(self, email):
        ("validating email")
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                print("email exists duh")
                raise ValidationError('Email already exists!')



class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = StringField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')