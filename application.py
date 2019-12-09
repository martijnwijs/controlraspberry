
import os
import requests
import csv

from flask import Flask, jsonify, render_template, request, redirect, send_file, session
from flask_socketio import SocketIO, emit
from models import *
from create import *
#app = Flask(__name__) # Instantiate a new web application called `app`, with `__name__` representing the current file

# what is this
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

# start socketio
socketio = SocketIO(app)


# handles controller page

#global variables
measurementname = ''

@app.route("/") 
def index():
    # get all current controllers
    controllers = Controller.query.all()
    return render_template("index.html", controllers=controllers)

# handles measurement page
@app.route("/measurements")
def measurements():
    measurements = Measurement.query.all()
    return render_template("measurements.html", measurements=measurements)

@app.route("/addcontroller", methods=["GET", "POST"]) 
def addcontroller():
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

@app.route("/addmeasurement", methods=["GET", "POST"]) 
def addmeasurement():
    if request.method == "GET":
        return render_template("addmeasurement.html")
    if request.method == "POST":

        name = request.form.get("name")
        pinnumber = request.form.get("pinnumber")
        ylabel = request.form.get("label")
        # add to database
        measurement = Measurement(name=name, pinnumber=pinnumber, ylabel=ylabel)
        db.session.add(measurement)
        db.session.commit()
        return redirect("/measurements")

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

# when receiving data updates 
@socketio.on("updatedata")
def updatedata(data):
    print("data: ", data)
    print("measurementname: ", session['record'], record)
    # if recording write to csv file
    if record == True and measurementname == str(data['measurementname']):
        print("writing to csv")
        filename = str(data['measurementname'].csv)
        file = open(filename, "a")
        writer = csv.writer(file)
        writer.writerow((data['time'], data['value']))
        file.close()
    emit("updatedata", data, broadcast=True)

# when user starts recording
@socketio.on("startrecording")
def startrecording(data):
    print("startrecording")
    measurementname = str(data['measurementname'])
    session['measurementname'] = str(data['measurementname'])
    session['record'] = 'True'
    return measurementname

# when user ends recording
@socketio.on("stoprecording")
def stoprecording(data):
    print("stoprecording")
    session['measurementname'] = str(data['measurementname'])
    session['record'] = 'False'
    return record, measurementname

