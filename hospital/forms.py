from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError
from hospital.models import User, Doctor

class UserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=6, max=15)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(),Length(min=6, max=15)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(),Length(min=6, max=15),EqualTo('password')])
    submit = SubmitField('Submit')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already exists')
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('A account already exists from this email')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class PatientForm(FlaskForm):
    firstName = StringField('First Name', validators=[DataRequired(), Length(min=2,max=20)])
    lastName = StringField('Last Name', validators=[DataRequired(), Length(min=2,max=20)])
    age = StringField('Age', validators=[DataRequired()])
    gender = StringField('Gender', validators=[DataRequired()])   
    submit = SubmitField('Submit')

class DoctorForm(FlaskForm):
    firstName = StringField('First Name', validators=[DataRequired(), Length(min=2,max=20)])
    lastName = StringField('Last Name', validators=[DataRequired(), Length(min=2,max=20)])
    age = StringField('Age', validators=[DataRequired()])
    gender = StringField('Gender', validators=[DataRequired()])   
    specialization = StringField('Specialization', validators=[DataRequired()]) 
    submit = SubmitField('Submit')