__==================Data Classes in models:===================__<br><br>
the data is gonna be stored  in sql through python classes
the controller class contains the controller objects <br><br>
__Class Controller:__<br>
    controllername<br><br>
  __Class User__<br>
 (from django library)<br> <br> 
 
 the project class contains all the data a certain project has .
 it links to the user, the  controllers and optionally ( if enought time ) the measurements.<br><br>

 __Class Project:__<br>
    user =(foreignkey User)<br>
    controllers= (manytomany Controller)<br>
    __optional__<br>
    measurements =(manytomany Timeseries)<br>
  
  __======optional timeseries ========__<br><br>
  the  timeseries class contains all the  datapoints objects of the measurements<br><br>
  __Class Timeseries__<br>
    ypoint (float)<br>
    timepoint (float)<br><br>
  
  The measurement class contains the measurement objects. the objects have name, labels  for both dimensions and a list  containing all the timeseries objects (datapoints)<br><br>
  __Class Measurement__<br>
      name (char)<br>
      ylabel  (char)<br>
      xlabel (char)<br>
      data = (manytomany Timeseries)<br><br>
   
   __===========================Urls==========================__<br><br>
    
  /login<br><br>
   /register<br><br>
    /"" <br>
    this page contains all he projects the user has created  so far. the user can open a project add  and  delete projects. <br><br>
/controller  
here the user can choose controllers<br><br>
/controller/add<br>
here  the user  can add controllers<br><br>
/setup<br>
the user learns how to setup the arduino code and connect the arduino with the webapp. for private sessions the user might fill in the IP adress of the arduino<br><br>
    
   /measurements<br>here the user can see the current measurements represenated in graphs <br><br>
   /measurements/add <br>here the user  can add measurements
    
    
   __====================Socket.IO============================__<br><br>
  here follows  some information about the websocket between the  arduino en the webserver.
 on the /controllerpage page , a switch is displayed haveing the options ON and OFF.
 there is a:
 - javascript eventlistener onclick emit "switchbutton=ON"

on the webserver there is a:
- @socket receives emit "switchbutton=ON"
  broadcast switchbutton="ON", such that the arduino cleint websocket can understand the message.

on the arduino, connected with wifi there is a:
- socket client receiving emit from webserver and translating this to controlling the led

    
