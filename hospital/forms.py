from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

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

