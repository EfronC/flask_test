from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Gender(db.Model):
	__tablename__ = 'gender'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Text, nullable=False)
	person = db.relationship('Person', backref='gender', lazy=True)

class Ethnicity(db.Model):
	__tablename__ = 'ethnicity'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Text, nullable=False)
	person = db.relationship('Person', backref='ethnicity', lazy=True)

class Person(db.Model):
	__tablename__ = 'person'

	id = db.Column(db.Integer, primary_key=True)
	fullname = db.Column(db.Text, nullable=True)
	gender_id = db.Column(db.Integer, db.ForeignKey('gender.id'), nullable=True)
	ethnicity_id = db.Column(db.Integer, db.ForeignKey('ethnicity.id'), nullable=True)

	def __repr__(self):
		return '<Person %r>' % self.fullname