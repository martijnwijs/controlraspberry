
from flask import Flask, render_template, request
import os
#import table definitions
from models import*

app = Flask(__name__) 

# Tell Flask what SQLAlchemy databas to use.
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgres://qfmxemjghejlho:c6d408838b454d4d58ca0eee78c5ef8426e76fccb2b49475dd61597595e14047@ec2-54-217-243-19.eu-west-1.compute.amazonaws.com:5432/dcrp4mj4mjflpb'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Link the Flask app with the database (no Flask app is actually being run yet).
db.init_app(app)

def main():
    # Create tables based on each table definition in `models`
    db.create_all()

if __name__ == "__main__":
    # Allows for command line interaction with Flask application
    with app.app_context():
        main()