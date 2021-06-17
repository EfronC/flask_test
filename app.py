import json
import requests

import flask

from flask import Flask, jsonify, request
from flask_cors import cross_origin
from flask_migrate import Migrate
from models import *
from util import callDiversity

db_path = "app.db"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+db_path
app.config['CORS_HEADERS'] = 'Content-Type'
db.init_app(app)
migrate = Migrate(app, db)

@app.route('/test/<string:name>', methods=['GET'])
def test(name):
	print(request.data)
	print(name)
	return jsonify({"test":"bar"})

@app.route('/persons/', methods=['POST'])
@cross_origin(origin='*',headers=['Content-Type'])
def savePerson():
	r = json.loads(request.data)
	fullname = r["fullname"]
	gender_id = r["gender"]
	ethnicity_id = r["ethnicity"]
	try:
		if fullname and gender_id and ethnicity_id:
			gender = Gender.query.filter_by(id=gender_id).first()
			ethnicity = Ethnicity.query.filter_by(id=ethnicity_id).first()
			if gender and ethnicity:
				person = Person(fullname=fullname, gender_id=gender_id, ethnicity_id=ethnicity_id)
				db.session.add(person)
				db.session.commit()
				p = Person.query.filter_by(id=person.id).first()
				if p:
					return jsonify({"stat":True, "msg": "Person saved"})
				else:
					return jsonify({"stat":False, "msg": "Something happened"})
			else:
				return jsonify({"stat":False, "msg": "Parameters incorrect"})
		else:
			return jsonify({"stat":False, "msg": "Missing data"})
	except Exception as e:
		print(e)
		return jsonify({"stat":False, "msg": "Internal error"})

@app.route('/persons/<string:name>', methods=['GET'])
@app.route('/persons/', defaults={'name': None}, methods=['GET'])
@cross_origin(origin='*',headers=['Content-Type'])
def checkPerson(name):
	try:
		if name:
			p = Person.query.filter(Person.fullname.contains(name)).first()
			if p:
				data = {"fullname":p.fullname, "gender":p.gender.name, "ethnicity":p.ethnicity.name}
				return jsonify({"stat":True, "data":data})
			else:
				p = callDiversity(name)
				if p:
					data = {"fullname":p["fullname"], "gender":p["gender"], "ethnicity":p["ethnicity"]}
					return jsonify({"stat":True, "data":data})
		else:
			ps = Person.query.all()
			if ps:
				persons = list()
				for i in ps:
					c = {"fullname":i.fullname, "gender":i.gender.name, "ethnicity":i.ethnicity.name}
					persons.append(c)
				data = {"persons":persons}
				return jsonify({"stat":True, "data":data})
	except Exception as e:
		print(e)
		return jsonify({"stat":False})

@app.route('/', methods=['GET'])
def index():
	return "<h1>Flask Test</h1><p>Nothing to see here.</p>"

if __name__ == '__main__':
	app.run(host='localhost', port=5010, threaded=True, debug=True)