I didn't payed a lot of attention on the following parts due to time restrictions:

- the login system. I mostly copied it from the books app and its far from a professional system. 

- the setup page and it's layout. 

- for the rest I payed a lot of attention to the backend as well as the styling/frontend. I spend a lot of time on Javascript code and making the  animation of the record button work.  I also made sure that the code ment for the raspberry PI was fully functional and that no code has to be written by the user. this code can be found by clientraspberry.py. I also made sure that multiple raspberries can be connected to one controller. 
The execute controller isn't working because one mistyped spelling on the controller page (see review.md), but is apart from that fully functional.

__design decisions__
1. switching from the arduino device to a raspberry PI. I did this because A the arduino didn't have a built in wifi connector and B the arduino didn't have a real socket library. It would be very hard if not impossible to realize this project for a arduino

2. chosing the Flask framework vs the Django framework. 
The pro's of Flask were the socket.io library, which makes socket connections relatively easy comparing to django channels.
the pro's of Django were the added functionality of login and admin.
With the flask application making all the sockets functional was already a task so in the timespan the question is how a django framework would have worked out. Im glad with the decision to use flask.
