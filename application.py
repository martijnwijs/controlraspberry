
import os
import io
import requests
import csv

from flask import Flask, jsonify, render_template, request, redirect, send_file, session,  current_app
from flask_socketio import SocketIO, emit
from models import *
from create import *

# hash password
from hash import*

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
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
    
        # check if username is in database
        data = Account.query.filter(Account.username == username).first() #check of dit niet hoeft
       
        # if not redirect to same page
        if data is None:
            return render_template("login.html", login=False)

        # check if hashed password is the given password by the user
        # if so start a session and redirect to search page
        if verify_password(data.passwordhashed, password):
            user = Account.query.filter(Account.username == username).first() #check of dit niet hoeft
            session['user'] = user.id
            return redirect("/")

    # else redirect to the same page
    return render_template("login.html", login=False)

# logout
@app.route("/logout", methods=["GET"])
def logout():
    session.pop("user", None)
    return redirect("/login")

# register
# navigate to register.html
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    if request.method == "POST":
        print("register")
        # get username and password
        username = request.form.get("username")
        password = request.form.get("password") 

        # check if username already in database
        username_check = Account.query.filter(Account.username == username).first() #check of dit niet hoeft
        print(username_check)
        if username_check != None: ## kijk wat dit geeft
            return render_template("register.html", available = False)

        # if username and or password is an empty string, redirect to same page with message
        if len(username) ==0 or len(password) == 0: 
            return render_template("register.html", characters = False)

        #Hash password
        passwordhashed = hash_password(password)

        # add user to database
        user = Account(username=username, passwordhashed=passwordhashed)
        db.session.add(user)
        db.session.commit()
        # start a private session

        user = Account.query.filter(Account.username == username).first() #check of dit niet hoeft
        session['user'] = user.id
        return redirect("/")

@app.route("/", methods=["GET", "POST"]) 
def index():
    if request.method == "GET":
        if not logged_in():
            return redirect("/login")
        # get all current controllers
        controllers = Controller.query.filter(Controller.user == session['user']).all()
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
        if not logged_in():
            return redirect("/login")

        measurements = Measurement.query.all()
        return render_template("measurements.html", measurements=measurements)
    if request.method == "POST":
        name = request.form['name']
        measurement = Measurement.query.filter(Measurement.name == name).delete()
        Measurement.query.filter(and_(Measurement.name == name, Measurement.user == session['user'])).all().delete()
        db.session.commit()
        return redirect("/measurements")

@app.route("/addcontroller", methods=["GET", "POST"]) 
def addcontroller():
    if request.method == "GET":
        if not logged_in():
            return redirect("/login")
        return render_template("addcontroller.html")

    if request.method == "POST":
        type = request.form.get("type")
        name = request.form.get("name")
        pinnumber = request.form.get("pinnumber")
        min = request.form.get("min")
        max = request.form.get("max")

        # add to database
        controller = Controller(type=type, name=name, pinnumber=pinnumber, min=min, max=max, user=session['user'])
        db.session.add(controller)
        db.session.commit()
        return redirect("/")

@app.route("/addmeasurement", methods=["GET", "POST"]) 
def addmeasurement():
    if request.method == "GET":
        if not logged_in():
            return redirect("/login")
        return render_template("addmeasurement.html")
    if request.method == "POST":

        name = request.form.get("name")
        pinnumber = request.form.get("pinnumber")
        ylabel = request.form.get("label")
        # add to database
        measurement = Measurement(name=name, pinnumber=pinnumber, ylabel=ylabel, user=session['user'])
        db.session.add(measurement)
        db.session.commit()
        return redirect("/measurements")

# handles download requests + add error handling # make safe for injection!!
@app.route("/download/<filename>")
def download_file(filename):
    if not logged_in():
        return redirect("/login")

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
    if not logged_in():
        return redirect("/login")
    return render_template("setup.html")
    
# receives switch event from javascript
@socketio.on("submitswitch") 
def vote(data):
    print(data)

    # split id's to make broadcasting to more users possible
    listid = data['sid'].split(',')
    for id in listid:
        emit("announceswitch", data, room=id)

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
        

    


