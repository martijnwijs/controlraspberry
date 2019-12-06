import socketio

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
    sio.wait()
except KeyboardInterrupt:
    quit()