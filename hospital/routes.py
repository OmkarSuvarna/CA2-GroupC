from flask import render_template, url_for, flash, redirect
from hospital import app
from hospital.forms import LoginForm, PatientForm
from hospital.models import Doctor, Patient

patient = [
    {
        'id':'100',
        'firstName' : 'John',
        'lastName' : 'Snow',
        'age' : '25',
        'gender' : 'Male'
    },
    {
        'id':'101',
        'firstName' : 'Arya',
        'lastName' : 'Stark',
        'age' : '20',
        'gender' : 'Female'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', patient=patient)

@app.route("/second-page")
def about():
    return "<h1>Second Page will go here</h1>"

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == 'omkar' and form.password.data == '123':
            flash(f'Welcome {form.username.data}', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', form=form)

@app.route("/register", methods=['GET', 'POST'])
def registerPatient():
    form = PatientForm()
    if form.validate_on_submit():
         flash(f'Added Patient : {form.firstName.data}', 'success')
         return redirect(url_for('registerPatient'))
    return render_template('registerPatient.html', form=form)