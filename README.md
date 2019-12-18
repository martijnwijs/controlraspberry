__project name:__ Control you Raspberry online

__purpose:__ To control a Raspberry PI via a webapp without the need to write any code yourself and to stream measurements and record them.

![image screenshots](/img/screenshots.jpg)

__files__ 
- application.py is the flask application
- create.py is used to update the database
- hash.py is used to hash password and to verify a password
- clientraspberry.py is the file which needs to be runned on the raspberry PI
- clientmeasurement.py is a file used to generate fake measurements to stream  them in the app. this file can easily be adapted to measure real stuff. 
- the templates folder contains all the html pages.
- the static folder contains the images and scss/css files.
- the designdocuments folder contains the design documents of the app.

all the how-to's can be found on the setup page of the application. 

__acknowledgements__
- hash.py: retrieved from https://www.vitoshacademy.com/hashing-passwords-in-python/
- bootstrap 
-icons (trashbin add sign) made by <a href=https://www.flaticon.com/authors/freepik from https://www.flaticon.com/
- record button by Andrew White https://codepen.io/aeewhite/pen/BjzbOL

(c)  Martijn Wijsman 2019 - All rights reserved

link to screencast: https://youtu.be/7zpgCM4YLhQ
