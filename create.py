
from flask import Flask, render_template, request
from flask_session import Session
import os
#import table definitions
from models import*

app = Flask(__name__) 

# Tell Flask what SQLAlchemy databas to use.
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgres://qfmxemjghejlho:c6d408838b454d4d58ca0eee78c5ef8426e76fccb2b49475dd61597595e14047@ec2-54-217-243-19.eu-west-1.compute.amazonaws.com:5432/dcrp4mj4mjflpb'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
# Link the Flask app with the database (no Flask app is actually being run yet).
db.init_app(app)

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

def main():
    # Create tables based on each table definition in `models`
    db.create_all()

 # Allows for command line interaction with Flask application
if __name__ == "__main__":
    with app.app_context():
        main()
        print("done")