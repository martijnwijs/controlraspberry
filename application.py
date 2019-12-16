import os
import csv
import fnmatch

from flask import Flask, render_template, request, redirect, send_file, session,  current_app
from flask_socketio import SocketIO, emit

# object relational mapping and initialization of app
from models import *
from create import *

# hash password
from hash import*

# start socketio
socketio = SocketIO(app)

#function that checks if the user is logged in
def logged_in():
    if session.get("user", None) is not None: 
        return True
    return False

# handles mainpage:
@app.route("/")
def main():
    if not logged_in():
        return redirect("/login")
    return redirect("/controller")

# handles login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
    
        # check if username is in database
        data = Account.query.filter(Account.username == username).first() 
       
        # if not redirect to same page
        if data is None:
            return render_template("login.html", login=False)

        # check if hashed password is the given password by the user
        # if so start a session and redirect to search page
        if verify_password(data.passwordhashed, password):
            user = Account.query.filter(Account.username == username).first() 
            session['user'] = user.id
            return redirect("/controller")

    # else redirect to the same page
    return render_template("login.html", login=False)

# handles logout
@app.route("/logout", methods=["GET"])
def logout():
    session.pop("user", None)
    return redirect("/login")

# handles register
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
        username_check = Account.query.filter(Account.username == username).first()
        print(username_check)
        if username_check != None: 
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
        user = Account.query.filter(Account.username == username).first() 
        session['user'] = user.id
        return redirect("/controller")

# handles controller page
@app.route("/controller", methods=["GET", "POST"]) 
def controller():
    if not logged_in():
        return redirect("/login")
    if request.method == "GET":

        # get all current controllers
        controllers = Controller.query.filter(Controller.user == session['user']).all()
        return render_template("controller.html", controllers=controllers, page="controllers")

    # delete controller
    if request.method == "POST":
        name = request.form['name']
        Controller.query.filter((Controller.name == name) & (Controller.user == session['user'])).delete()
        db.session.commit()
        return redirect("/controller")

# handles measurement page
@app.route("/measurements", methods=["GET", "POST"])
def measurements():
    if not logged_in():
        return redirect("/login")
    if request.method == "GET":
        measurements = Measurement.query.filter(Measurement.user == session['user']).all()
        return render_template("measurements.html", measurements=measurements, page="measurements")

    # delete measurement
    if request.method == "POST":
        name = request.form['name']
        Measurement.query.filter((Measurement.name == name) & (Measurement.user == session['user'])).delete()
        db.session.commit()
        return redirect("/measurements")

# handles adding a controller
@app.route("/addcontroller", methods=["GET", "POST"]) 
def addcontroller():
    if not logged_in():
        return redirect("/login")
    if request.method == "GET":
        return render_template("addcontroller.html", page="controllers")

    if request.method == "POST":
        if not logged_in():
            return redirect("/login")
        type = request.form.get("type")
        name = request.form.get("name")
        pinnumber = request.form.get("pinnumber")
        min = request.form.get("min")
        max = request.form.get("max")
        print("Name: ",name)

        # make sure that the user has filled in the forms
        if type == "" or name == "" or pinnumber == "":
            return render_template("addcontroller.html", message=True, page="controllers")

        # make sure min and max are different
        if type == "slider" and min == max:
            return render_template("addcontroller.html", message2=True, page="controllers")

        # check if the name is already used by the user
        check = Controller.query.filter((Controller.name == name) & (Controller.user == session['user'])).all()
        if len(check) > 0:
            return render_template("addcontroller.html", page="controllers", message3=True)
        # add to database and redirect
        controller = Controller(type=type, name=name, pinnumber=pinnumber, min=min, max=max, user=session['user'])
        db.session.add(controller)
        db.session.commit()
        return redirect("/controller")

# handles adding a measurement
@app.route("/addmeasurement", methods=["GET", "POST"]) 
def addmeasurement():
    if not logged_in():
        return redirect("/login")
    if request.method == "GET":
        return render_template("addmeasurement.html", page="measurements")
        
    if request.method == "POST":
        name = request.form.get("name")

        # give a default pinnumber, measurements do not contain any pinnumbers
        pinnumber = 0
        ylabel = request.form.get("label")

        # check if the forms are filled in
        if name == "" or ylabel == "":
            return render_template("addmeasurement.html", page="measurements", message=True)

        # check if the name is already used by the user
        check = Measurement.query.filter((Measurement.name == name) & (Measurement.user == session['user'])).all()
        if len(check) > 0:
            return render_template("addmeasurement.html", page="measurements", message2=True)

        # add to database
        measurement = Measurement(name=name, pinnumber=pinnumber, ylabel=ylabel, user=session['user'])
        db.session.add(measurement)
        db.session.commit()
        return redirect("/measurements")

# handles download requests 
@app.route("/download/<filename>")
def download_file(filename):
    if not logged_in():
        return redirect("/login")

    # security to make sure the user can only download csv files
    if not fnmatch.fnmatch(filename, '*.csv'):
        return redirect("/measurements")
    file_path = str(filename)

    # handles filerequests that don't exist
    try:
        file_handle = open(file_path, 'r')
    except FileNotFoundError:
        return redirect("/measurements")

    # store file temporary
    def stream_and_remove_file():
        yield from file_handle
        file_handle.close()
        os.remove(file_path)
    return current_app.response_class(
        stream_and_remove_file(),
        headers={f'Content-Disposition': 'attachment; filename: {filename}; mimetype=text/csv', 'Content-Type': 'text/csv'}
    )

# handles setup page
@app.route("/setup") 
def setup():
    if not logged_in():
        return redirect("/login")
    return render_template("setup.html", page="setup")
    
# receives switch event from javascript
@socketio.on("submitswitch") 
def vote(data):
    print(data)
    
    # split id's to make broadcasting to more users possible
    listid = data['sid'].split(',')
    for id in listid:
        emit("announceswitch", data, room=id)

# when receiving data updates 
@socketio.on("updatedata")
def updatedata(data):
    emit("updatedata", data, broadcast=True)

# when user starts recording
@socketio.on("recording")
def recording(data):
    filename = str(data['measurementname'])+".csv"
    file = open(filename, "a+")
    writer = csv.writer(file)
    writer.writerow((data['time'], data['value']))
    file.close()