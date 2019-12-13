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
while True:
    now = datetime.datetime.now()
    hour = '{:02d}'.format(now.hour)
    minute = '{:02d}'.format(now.minute)
    second = '{:02d}'.format(now.second)
    x = '{}-{}-{}'.format(hour, minute, second)
    y = randint(0, 10)

    data = (x,y)
    print(data)
    
    sio.emit("updatedata", {'measurementname': 'sdf','time': x, 'value': y})
    time.sleep(1)
