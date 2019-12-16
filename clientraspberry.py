import socketio
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False)
 
sio = socketio.Client()

# put here your code execution methods
# make sure you make the name of your method equal to the name of your controller in de app
# the method below is an example where a led blinks two times when executed
def blink(value):
    if value == "HIGH":
        print("LED on")
        GPIO.output(17,GPIO.HIGH)
        time.sleep(1)
        print("LED off")
        GPIO.output(17,GPIO.LOW)
        time.sleep(1)
        print("LED on")
        GPIO.output(17,GPIO.HIGH)
        time.sleep(1)
        print("LED off")
        GPIO.output(17,GPIO.LOW)
        time.sleep(1)

# def yourcontrollername(value): 
   

# connection and disconnection             
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

# code to give a boolean output or duty cycle to the pin
# nothing needs to be changed here
@sio.on("announceswitch")
def switch(data):

    # if toggle switch
    if data['type'] == "toggle":
        GPIO.setmode(GPIO.BCM)
        dictoutput={'LOW': GPIO.LOW, 'HIGH': GPIO.HIGH}
        GPIO.setup(dictpins[data['pin']],GPIO.OUT)
        GPIO.output(dictpins[data['pin']],dictoutput[data['value']])
        
    # if slider 
    if data['type'] == "slider":
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(int([data['pin']), GPIO.OUT)
        pwm = GPIO.PWM(int(data['pin']),50)
        pwm.start(0)
        pwm.ChangeDutyCycle(int(data['value']))
        time.sleep(0.2)
        pwm.stop()
        GPIO.cleanup()
        
    # if execute code
    if data['type'] == "execute":
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(int([data['pin'], GPIO.OUT)
        globals()[data['name']](data['value'])
        

       
sio.connect('http://172.20.10.4:5000/') # fill in here the webadress of the app to create a socket connection
try:
    sio.sleep(1)
except KeyboardInterrupt:
    quit()

