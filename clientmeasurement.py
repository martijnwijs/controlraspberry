import socketio
import time
from random import randint
import datetime


sio = socketio.Client()

@sio.event
def connect():
    print('connection established')
    sio.emit('test',{'hoi': 'hoi'})
    print('my sid is', sio.sid)

@sio.event
def disconnect():
    print('disconnected from server')
    quit()

@sio.event
def connect_error():
    print("The connection failed!")

@sio.on("announceswitch")
def on_message(data):
    print('I received a message!')
    print(data)

sio.connect('http://127.0.0.1:5000/')
try:
    sio.sleep(1)
except KeyboardInterrupt:
    quit()


x=0
y=1.

# handling measurements
def measure():
    while True:
        now = datetime.datetime.now()
        hour = '{:02d}'.format(now.hour)
        minute = '{:02d}'.format(now.minute)
        second = '{:02d}'.format(now.second)
        x = '{}-{}-{}'.format(hour, minute, second)

        # get here your Y value from GPIO sensor data or something else...
        y = randint(0, 10)
    
        # fill in here your measurementname, it should be the same as the name of the measurementname in the App
        measurementname = ""

        # fill in here your timestep between two measurements.
        timestep = 1

        sio.emit("updatedata", {'measurementname': measurementname,'time': x, 'value': y})
        time.sleep(timestep) # change this to change the time interval between two data points
measure()
