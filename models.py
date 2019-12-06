from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# class containing all the controllers
class Controller(db.Model):
    __tablename__="controllers"
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    pinnumber = db.Column(db.Integer, nullable=False)
    min = db.Column(db.String, nullable=True)
    max = db.Column(db.String, nullable=True)
    
