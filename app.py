import os
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from db import db


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI', 'sqlite:///newdata.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class fixdb(db.Model):
	__tablename__ = 'dht_new'

	id = db.Column(db.Integer, primary_key =True)
	name = db.Column(db.String(80))


	def __init__(self, temp):
		self.temp = temp

	def add_to_db(self):
		db.session.add(self)
		db.session.commit()


@app.route('/get', methods=['GET'])
def postrandom():
	temp = {'temperature': '23'}
	db.create_all() 
	test_temp = fixdb(temp)
	test_temp.add_to_db()
	return jsonify(temp)

@app.route('/list', methods=['GET'])
def postrandom():
	temp = {'temperature': '23'}
	db.create_all() 
	test_temp = fixdb(temp)
	test_temp.add_to_db()
	return jsonify(temp)


if __name__ == '__main__':
	app.run(port=5000, debug=True)