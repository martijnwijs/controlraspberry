
import os
import requests

from flask import Flask, jsonify, render_template, request, redirect
from flask_socketio import SocketIO, emit
from models import *
from create import *
#app = Flask(__name__) # Instantiate a new web application called `app`, with `__name__` representing the current file

# what is this
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

# start socketio
socketio = SocketIO(app)



@app.route("/") 
def index():
    # get all current controllers
    controllers = Controller.query.all()
    return render_template("index.html", controllers=controllers)

@app.route("/addcontroller", methods=["GET", "POST"]) 
def controller():
    if request.method == "GET":
        return render_template("addcontroller.html")
    if request.method == "POST":
        type = request.form.get("type")
        name = request.form.get("name")
        pinnumber = request.form.get("pinnumber")
        min = request.form.get("min")
        max = request.form.get("max")

        # add to database
        controller = Controller(type=type, name=name, pinnumber=pinnumber, min=min, max=max)
        db.session.add(controller)
        db.session.commit()
        return redirect("/")

@socketio.on("submitswitch") # receives switch event from javascript
def vote(data):
    print(data)
    selection = data["selection"]
    #pin = data["pin"]
    
    print(selection)
    #print("pin: ", pin)
    emit("announceswitch", {"selection": selection}, broadcast=True)

@socketio.on("test") #from python script
def nietslim(data):
    print("hallo")



