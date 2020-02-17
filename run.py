from app import app
from app import create_tables

db.init_app(app)
@app.before_first_request
def create_tables():
	db.create_all()