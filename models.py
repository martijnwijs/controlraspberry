from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# class containing all the accounts
class Account(db.Model):
    __tablename="accounts"
    id = db.Column(db.Integer, primary_key=True) #user id
    username = db.Column(db.String, nullable=False)
    passwordhashed = db.Column(db.String, nullable=False)

# class containing all the controllers
class Controller(db.Model):
    __tablename__="controllers"
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, db.ForeignKey("account.id"), nullable=False)
    type = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    pinnumber = db.Column(db.Integer, nullable=False)
    min = db.Column(db.String, nullable=True)
    max = db.Column(db.String, nullable=True)

# class containing all the measurements
class Measurement(db.Model):
    __tablename__="measurements" 
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, db.ForeignKey("account.id"), nullable=False)
    name = db.Column(db.String, nullable=False)
    pinnumber = db.Column(db.Integer, nullable=False)
    ylabel = db.Column(db.String, nullable=True)   



#class Datapoint(db.Model):
    #__tablename__="datapoints"
    #id = db.Column(db.Integer, primary_key=True)
    #id = db.Column(db.Integer, db.ForeignKey("measurements.id"), nullable=False)
   # ypoint = db.Column(db.Integer, nullable=False)
    # timepoint = db.Column(db.String, nullable=False)

    
