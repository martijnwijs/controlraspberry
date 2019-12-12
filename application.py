
import os
import io
import requests
import csv

from flask import Flask, jsonify, render_template, request, redirect, send_file, session,  current_app
from flask_socketio import SocketIO, emit
from models import *
from create import *
#app = Flask(__name__) # Instantiate a new web application called `app`, with `__name__` representing the current file

# what is this
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")


# start socketio
socketio = SocketIO(app)

#function that checks  if the user is logged in:
def logged_in():
    #check if user is logged in
    if session.get("user", None) is not None: 
        return True
    return False
# handles controller page

#global variables
measurementname = ''

# handles login
@app.route("/login", methods=["GET", POST])
def login():
    if request.method == "GET":

        username = request.form.get("username")
        password = request.form.get("password")
    
        # check if username is in database
        data = db.execute("SELECT * FROM accounts WHERE username = :username", {"username": username}).fetchone()
    
        # if not redirect to same page
        if data is None:
            return render_template("index.html", login = False)

        # check if hashed password is the given password by the user
        # if so start a session and redirect to search page
        if verify_password(data.password, password):
            user = db.execute("SELECT * FROM accounts WHERE username = :username", {"username": username}).fetchone()
            session['user'] = user.id
            return redirect("/search")

    # else redirect to the same page
    return render_template("index.html", login = False)

@app.route("/", methods=["GET", "POST"]) 
def index():
    if request.method == "GET":
        # get all current controllers
        controllers = Controller.query.all()
        return render_template("index.html", controllers=controllers)
    if request.method == "POST":
        name = request.form['name']
       
        controller = Controller.query.filter(Controller.name == name).delete()
        #print(controller)
        #db.session.delete(controller)
        db.session.commit()
        return redirect("/")
# handles measurement page
@app.route("/measurements", methods=["GET", "POST"])
def measurements():
    if request.method == "GET":
        measurements = Measurement.query.all()
        return render_template("measurements.html", measurements=measurements)
    if request.method == "POST":
        name = request.form['name']
        measurement = Measurement.query.filter(Measurement.name == name).delete()
        db.session.commit()
        return redirect("/measurements")

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

# handles download requests + add error handling # make safe for injection!!
@app.route("/download/<filename>")
def download_file(filename):
    file_path = filename
    file_handle = open(file_path, 'r')

    # This *replaces* the `remove_file` + @after_this_request code above
    def stream_and_remove_file():
        yield from file_handle
        file_handle.close()
        os.remove(file_path)

    return current_app.response_class(
        stream_and_remove_file(),
        headers={f'Content-Disposition': 'attachment; filename: {filename}; mimetype=text/csv', 'Content-Type': 'text/csv'}
    )

@app.route("/setup") 
def setup():
    return render_template("setup.html")
    
# receives switch event from javascript
@socketio.on("submitswitch") 
def vote(data):
    print(data)
    emit("announceswitch", data, broadcast=True)

@socketio.on("test") #from python script
def nietslim(data):
    print("hallo")

# when receiving data updates 
@socketio.on("updatedata")
def updatedata(data):
    print("data: ", data)
    
    emit("updatedata", data, broadcast=True)

# when user starts recording
@socketio.on("recording")
def recording(data):
    print("recording")

    filename = str(data['measurementname'])+".csv"
    print(filename)
    file = open(filename, "a+")
    writer = csv.writer(file)
    writer.writerow((data['time'], data['value']))
    file.close()
    #return measurementname

# when user ends recording
#@socketio.on("stoprecording")
#def stoprecording(data):
    #print("stoprecording")
    #filename = str(data['measurementname'])+".csv"
    #return send_file(filename)

    '''
    try:
        filename = str(data['measurementname'])+".csv"
        with open(filename, 'r') as file:
            pass
        
    except FileNotFoundError:
        pass
        '''
        

    


