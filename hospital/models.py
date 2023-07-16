from datetime import datetime
from hospital import db

class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    usertype = db.Column(db.String(20), nullable=False)
    patients = db.relationship('Patient', backref='doctor', lazy=True)

    def __repr__(self):
        return f"Doctor('{self.username}','{self.usertype}')"


class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(20), nullable=False)
    lastName = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'), nullable=False)

    def __repr__(self):
        return f"Patient('{self.firstName}','{self.lastName}','{self.age}','{self.gender}')"
