import os
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from db import db


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class fixdb(db.Model):
	__tablename__ = 'dht_new'

	id = db.Column(db.Integer, primary_key =True)
	temp = db.Column(db.String(80))
	name = db.Column(db.String(80))

	def __init__(self, temp, name):
		self.temp = temp
		self.name = name


	def add_to_db(self):
		db.session.add(self)
		db.session.commit()

	def delete_from_db(self):
		db.session.delete(self)
		db.session.commit()




@app.route('/create', methods=['POST'])
def postrandom():
	data = request.get_json()
	temp = data['temp']
	name = data['name']
	test_temp = fixdb(temp, name)
	test_temp.add_to_db()
	print(temp)
	print(name)
	return jsonify(temp, name)
	return{'message', 'error'}

@app.route('/list', methods=['GET'])
def list():
	list = db.session.query(fixdb.temp, fixdb.name).all()
	for m in list:
		print(m)
	return jsonify(list)

@app.route('/name/<string:name>', methods=['GET'])
def getindex(name):
	if fixdb.query.filter_by(name=name).first():
		return {"index": ['name:', name]}


@app.route('/delete/<string:name>', methods=['POST'])
def delete(name):
	data = request.get_json()
	print(name)
	object = fixdb.query.filter_by(name=name).first()
	print(name)
	fixdb.delete_from_db(object)	
	return jsonify("deleted", name)


@app.route('/dht_receive', methods=['GET', 'POST'])
def input():
	if request.method == 'POST':
		tempan = request.form.get('temperature')
		return jsonify(tempan)


@app.route('/dht', methods=['GET'])
def getdht():
	data = request.get.json()
	temperature = data['temperature']
	return {'message:', 'temperature'}


	 

if __name__ == '__main__':
	db.create_all()
	app.run(host= '0.0.0.0', debug=True)