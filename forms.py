from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField, PasswordField,SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo

class RegistrationForm(FlaskForm):
    fname= StringField('First Name', validators=[DataRequired() ,Length(min=4, max=25)])
    lname = StringField('Last Name', validators=[DataRequired() ,Length(min=4, max=25)])
    username = StringField('Username', validators=[DataRequired() ,Length(min=4, max=25)])
    email = StringField('Email Address', validators=[DataRequired() ,Email()])
    password = PasswordField('Password',validators=[
        DataRequired(),
        Regexp("^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$")
    ])
    confirm_password = PasswordField('Repeat Password',validators=[EqualTo('password'),DataRequired()])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email',validators=[Email(),DataRequired()])
    password = PasswordField('password',validators=[DataRequired()])
    submit = SubmitField('Log In')
    remember = BooleanField('Remember Me')