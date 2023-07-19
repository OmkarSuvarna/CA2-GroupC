from datetime import datetime
from hospital import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    # usertype = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"User('{self.username}','{self.email}')"

# class Doctor2(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(20), unique=True, nullable=False)
#     password = db.Column(db.String(60), nullable=False)
#     usertype = db.Column(db.String(20), nullable=False)
#     patients = db.relationship('Patient', backref='doctor', lazy=True)

#     def __repr__(self):
#         return f"Doctor('{self.username}','{self.usertype}')"

class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(20), nullable=False)
    lastName = db.Column(db.String(20), nullable=False)
    age = db.Column(db.String(20), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    specialization = db.Column(db.String(10), nullable=False)
    patients = db.relationship('Patient', backref='doctor', lazy=True)

    def __repr__(self):
        return f"Doctor('{self.firstName}','{self.lastName}','{self.age}','{self.gender}','{self.specialization}')"

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(20), nullable=False)
    lastName = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'), default=None)
    # doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'), nullable=False)
    consultations = db.relationship('Consultation', backref='consultation', lazy=True)

    def __repr__(self):
        return f"Patient('{self.firstName}','{self.lastName}','{self.age}','{self.gender}')"
class Consultation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_consultation = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    description = db.Column(db.String(500), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), default=None)

    def __repr__(self):
        return f"Consultation('{self.date_consultation}','{self.description}',{self.patient_id})"
