import os
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from db import db


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI', 'sqlite:///newdata.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.before_first_request
def create_tables():
    db.create_all()


class fixdb(db.Model):
	__tablename__ = 'dht'

	id = db.Column(db.Integer, primary_key =True)
	name = db.Column(db.String(80))


	def __init__(self, temp):
		self.temp = temp

	def add_to_db(self):
		db.create_all()
		db.session.add(self)
		db.session.commit()


@app.route('/get', methods=['GET'])
def postrandom():
	temp = {'temperature': '23'}
	test_temp = fixdb(temp)

	test_temp.add_to_db()

	return jsonify(temp)



if __name__ == '__main__':
	from db import db
	db.init_app(app)
	app.run(port=5000, debug=True)