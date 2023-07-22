from flask import render_template, url_for, flash, redirect, request, abort
from hospital import app, db, bcrypt
from hospital.forms import LoginForm, PatientForm, UserForm, DoctorForm, ConsultationForm
from hospital.models import User, Doctor, Patient, Consultation 
from flask_login import login_user, current_user, logout_user, login_required

@app.route("/")
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash(f'Welcome {form.username.data}', 'success')
            return redirect(url_for('home_doctor'))         
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', form=form)

@app.route("/home_doctor", methods=['GET', 'POST'])
def home_doctor():
    form = PatientForm()
    if form.validate_on_submit():
        patient = Patient(firstName=form.firstName.data, lastName=form.lastName.data, age=form.age.data, gender=form.gender.data, doctor_id=1)
        db.session.add(patient)
        db.session.commit()
        flash(f'Added Patient : {form.firstName.data}  {form.lastName.data}', 'success')
        db.create_all()
        return redirect(url_for('home_doctor'))
    page = request.args.get('page', 1, type=int)
    patients = Patient.query.paginate(page=page, per_page=5)
    return render_template('home_doctor.html', form=form, patients=patients)

@app.route("/patient_profile/<int:patient_id>")
def patient_profile(patient_id):
    page = request.args.get('page', 1, type=int)
    patient = Patient.query.get_or_404(patient_id)
    consultation = Consultation.query.filter_by(patient_id=patient_id).paginate(page=page, per_page=5)
    return render_template('patient_profile.html', title ='Patient Profile', patient=patient, consultation=consultation)

@app.route("/patient_page/<int:patient_id>/update", methods=['GET', 'POST'])
def updatePatient(patient_id):
    patient = Patient.query.get_or_404(patient_id)
    # if patient.doctor != current_user:
    # abort(403)
    form = PatientForm()
    if form.validate_on_submit():
        patient.firstName = form.firstName.data
        patient.lastName = form.lastName.data
        patient.age = form.age.data
        patient.gender = form.gender.data
        db.session.commit()
        flash('Patient Details Updated', 'info')
        return redirect(url_for('home_doctor'))
    elif request.method == 'GET':
        form.firstName.data = patient.firstName
        form.lastName.data = patient.lastName
        form.age.data = patient.age
        form.gender.data = patient.gender
    return render_template('update_patient.html', title ='Update Patient', form=form, patient=patient)

@app.route("/home_doctor/<int:patient_id>/delete", methods=['GET'])
def deletePatient(patient_id):
    patient = Patient.query.get_or_404(patient_id)
    # if patient.doctor != current_user:
    # abort(403)
    db.session.delete(patient)
    db.session.commit()
    flash('Patient Details Deleted', 'info')
    return redirect(url_for('home_doctor'))

# customertype required
@app.route("/admin-useradd", methods=['GET', 'POST'])
def admin():
    form = UserForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('admin.html', form=form, title ='Add User')

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))

# @app.route("/register", methods=['GET', 'POST'])
# def registerPatient():
#     form = PatientForm()
#     if form.validate_on_submit():
#          flash(f'Added Patient : {form.firstName.data}', 'success')
#          return redirect(url_for('registerPatient'))
#     return render_template('registerPatient.html', form=form)    

#Admin adds Doctors
@app.route("/admin_addDoctor", methods=['GET', 'POST'])
def admin_addDoctor():
    form = DoctorForm()
    if form.validate_on_submit():
        doctor = Doctor(firstName=form.firstName.data, lastName=form.lastName.data, age=form.age.data, gender=form.gender.data, specialization=form.specialization.data)
        db.session.add(doctor)
        db.session.commit()
        flash(f'Added Doctor : {form.firstName.data} {form.lastName.data}', 'success')
        return redirect(url_for('admin_addDoctor'))
    # doctors = Doctor.query.all()
    page = request.args.get('page', 1, type=int)
    doctors = Doctor.query.paginate(page=page, per_page=5)
    return render_template('admin_addDoctor.html', form=form, title ='Add Doctor', doctors=doctors)

@app.route("/doctor_profile/<int:doctor_id>")
def doctor_profile(doctor_id):
    doctor = Doctor.query.get_or_404(doctor_id)
    return render_template('doctor_profile.html', title ='Doctor Profile', doctor=doctor)

@app.route("/doctor_page/<int:doctor_id>/update", methods=['GET', 'POST'])
def updateDoctor(doctor_id):
    doctor = Doctor.query.get_or_404(doctor_id)
    # if patient.doctor != current_user:
    # abort(403)
    form = DoctorForm()
    if form.validate_on_submit():
        doctor.firstName = form.firstName.data
        doctor.lastName = form.lastName.data
        doctor.age = form.age.data
        doctor.gender = form.gender.data
        doctor.specialization = form.specialization.data
        db.session.commit()
        flash(f'Doctor Details Updated', 'info')
        return redirect(url_for('admin_addDoctor'))
    elif request.method == 'GET':
        form.firstName.data = doctor.firstName
        form.lastName.data = doctor.lastName
        form.age.data = doctor.age
        form.gender.data = doctor.gender
        form.specialization.data = doctor.specialization
    return render_template('update_doctor.html', title ='Update Doctor', form=form, doctor=doctor)

@app.route("/admin_addDoctor/<int:doctor_id>/delete", methods=['GET'])
def deleteDoctor(doctor_id):
    doctor = Doctor.query.get_or_404(doctor_id)
    # if patient.doctor != current_user:
    # abort(403)
    db.session.delete(doctor)
    db.session.commit()
    flash('Doctor Details Deleted', 'info')
    return redirect(url_for('admin_addDoctor'))

@app.route("/patient_consultation/<int:patient_id>", methods=['GET', 'POST'])
def patientConsultation(patient_id):
    form = ConsultationForm()
    if form.validate_on_submit():
        consultation = Consultation(description=form.description.data, patient_id=patient_id)
        db.session.add(consultation)
        db.session.commit()
        flash('Added Consultation Details', 'success')
        # consultation = Consultation.query.filter_by(patient_id=patient_id)
        page = request.args.get('page', 1, type=int)
        consultation = Consultation.query.filter_by(patient_id=patient_id).paginate(page=page, per_page=5)
        return redirect(url_for('patient_profile', patient_id=patient_id, consultation=consultation))
    return render_template('patient_consultation.html', title ='Add Consultation', form=form)

