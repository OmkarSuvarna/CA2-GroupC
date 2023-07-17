from flask import render_template, url_for, flash, redirect
from hospital import app, db, bcrypt
from hospital.forms import LoginForm, PatientForm, UserForm
from hospital.models import User, Doctor, Patient 

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

@app.route("/admin-useradd", methods=['GET', 'POST'])
def admin():
    form = UserForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('A New User is Added', 'success')
        return redirect(url_for('home'))
    return render_template('admin.html', form=form)

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