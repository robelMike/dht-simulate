from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from db import db


app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

class fixdb(db.Model):
	__tablename__= 'dht'

	id = db.Column(db.Integer, primary_key =True)
	name = db.Column(db.String(80))

@app.route('/get', methods=['GET'])
def postrandom():
	temp = {'temperature': '23'}
	db.session.add(temp)
	db.session.commit()

	return jsonify(temp)



if __name__ == '__main__':
	app.run(port=5000)