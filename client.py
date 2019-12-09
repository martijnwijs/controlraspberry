import socketio
import time
 
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
    x = x + 1
    y =  y*1.75

    data = (x,y)
    print(data)
    
    sio.emit("updatedata", {'measurementname': 'sdf','time': x, 'value': y})
    time.sleep(1)