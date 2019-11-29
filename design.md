__Data Classes in models:__
the data is gonna be stored  in sql through python classes
the controller class contains the controller objects 
__Class Controller:__\
  controllername
 
 the project class contains all the data a certain project has .
 it links to the user, the  controllers and optionally ( if enought time ) the measurements.
 __Class Project:__\
  user =(foreignkey User)\
  controllers= (manytomany Controller)\
  __optional__\
  measurements =(manytomany Timeseries)\
  
  __optional__\
  the  timeseries class contains all the  datapoints objects of the measurements
  __Class Timeseries__\
    ypoint (float)\
    timepoint (float)\
  
  The measurement class contains the measurement objects. the objects have name, labels  for both dimensions and a list  containing all the timeseries objects (datapoints)
  __Class Measurement__\
    name (char)\
    ylabel  (char)\
    xlabel (char)\
    data = (manytomany Timeseries)\
    
   __Urls__
    
  /login
   /register
    /"" __overview page__ this page contains all he projects the user has created  so far.\the user can open a project add  and  delete projects. 
    /controller __controller page__ where the user can choose controllers
    /controller/add here  the user  can add controllers
    /setup  __setuppage__ the user learns how to setup the arduino code and connect the arduino with the webapp. for private sessions the user might fill in the IP adress of the arduino
    
  __optional__
   /measurementshere the user can see the current measurements represenated in graphs 
   /measurements/add here the user  can add measurements
    
    
   __socket.IO__
  here follows  some information about the websocket between the  arduino en the webserver.
 on the /controllerpage page , a switch is displayed haveing the options ON and OFF.
 there is a:
 - javascript eventlistener onclick emit "switchbutton=ON"

on the webserver there is a:
- @socket receives emit "switchbutton=ON"
  broadcast switchbutton="ON", such that the arduino cleint websocket can understand the message.

on the arduino, connected with wifi there is a:
- socket client receiving emit from webserver and translating this to controlling the led

    
