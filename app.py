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
		db.session.remove(self)
		db.session.commit()

	def __repr__(self):
		return {'temp:' + self.temp, 'name:' + self.name}


@app.route('/get', methods=['GET'])
def postrandom():
	tempa = {'message': 'LISTCREATED'}
	test_temp = fixdb(temp = '24', name = 'kobe')
	#test_tempan = fixdb(temp = '23', name = 'jordan')
	test_temp.add_to_db()
	#test_tempan.add_to_db()
	return jsonify(tempa)
	return{'message', 'error'}

@app.route('/list', methods=['GET'])
def list():
	list = db.session.query(fixdb.temp, fixdb.name).all()
	for m in list:
		print(m)

	return {"list": m}
	 
@app.route('/delete', methods=['delete'])
def delete():

	object = db.session.query(fixdb.temp, fixdb.name).all()
	fixdb.delete_from_db(object)
	return {'message:' 'f{object} is deleted'}
	 

if __name__ == '__main__':
	db.create_all()
	app.run(port=5000, debug=True)