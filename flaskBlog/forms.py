from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo,ValidationError
from email_validator import validate_email
from flaskBlog.models import User
from flask_login import current_user


class RegistrationForm(FlaskForm):
    username = StringField('Username', 
                            validators=[DataRequired(),Length(min=2, max=20)])
    email = StringField('Email', 
                            validators=[DataRequired(), Email()])
    password = PasswordField('Password', 
                            validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', 
                            validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')
    
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first
        if user:
            raise ValidationError('That username is taken. Please choose another one.')
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first
        if user:
            raise ValidationError('That email is already used. Please login or choose another one.')
        
        
class LoginForm(FlaskForm):
    email = StringField('Email', 
                            validators=[DataRequired(), Email()])
    password = PasswordField('Password', 
                            validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
    
    

class UpdateAccountForm(FlaskForm):
    username = StringField('Username', 
                            validators=[DataRequired(),Length(min=2, max=20)])
    email = StringField('Email', 
                            validators=[DataRequired(), Email()])
    submit = SubmitField('Update')
    
    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first
            if user:
                raise ValidationError('That username is taken. Please choose another one.')
    
    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first
            if user:
                raise ValidationError('That email is already used. Please login or choose another one.')