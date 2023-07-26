from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError
# from wtforms.ext.sqlalchemy.fields import QuerySelectField
from hospital.models import User, Doctor, Consultation

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
    gender = SelectField('Gender', coerce=str, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Others')])
    doctor = SelectField('Primary Doctor', coerce=str)
    submit = SubmitField('Submit')

    #taken from https://kyle.marek-spartz.org/posts/2014-04-04-setting-wtforms-selection-fields-dynamically.html
    def __init__(self):
        super(PatientForm, self).__init__()
        self.doctor.choices = [(d.id, d.firstName +' '+ d.lastName) for d in Doctor.query.all()]

class DoctorForm(FlaskForm):
    firstName = StringField('First Name', validators=[DataRequired(), Length(min=2,max=20)])
    lastName = StringField('Last Name', validators=[DataRequired(), Length(min=2,max=20)])
    age = StringField('Age', validators=[DataRequired()])
    gender = SelectField('Gender', coerce=str, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Others')])
    # specialization = StringField('Specialization', validators=[DataRequired()])
    specialization = SelectField('Specialization', coerce=str, choices=[('Pediatrics', 'Pediatrics'), ('Orthopedics', 'Orthopedics'), ('Surgeon', 'Surgeon'),('Neurology', 'Neurology'),('Anesthesiology', 'Anesthesiology'),('Orthodontics', 'Orthodontics'),('Ophthalmology', 'Ophthalmology'),('Psychiatry', 'Psychiatry')])
    submit = SubmitField('Submit')

class ConsultationForm(FlaskForm):
    description = TextAreaField('Consultation Details', validators=[DataRequired()])
    doctor = SelectField('Doctor', coerce=str)
    submit = SubmitField('Submit')

     #taken from https://kyle.marek-spartz.org/posts/2014-04-04-setting-wtforms-selection-fields-dynamically.html
    def __init__(self):
        super(ConsultationForm, self).__init__()
        self.doctor.choices = [(d.id, d.firstName +' '+ d.lastName) for d in Doctor.query.all()]