import socketio
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)#BOARD
GPIO.setwarnings(False)
 
sio = socketio.Client()
# dictionary for pins
valueglob = "LOW" 
## put here your execute methods
def blink(value):
    global valueglob
    if value == "HIGH": #do this
        
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
        
    if value =="LOW" : #do that
        GPIO.output(17,GPIO.LOW)
        
        
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
def switch(data):
    # if toggle switch
    if data['type'] == "toggle":
        dictpins = {'1': 1, '17': 17}
        GPIO.setmode(GPIO.BCM)
        dictoutput={'LOW': GPIO.LOW, 'HIGH': GPIO.HIGH}
        GPIO.setup(dictpins[data['pin']],GPIO.OUT)
        GPIO.output(dictpins[data['pin']],dictoutput[data['value']])
        
    # if slider
    if data['type'] == "slider":
        dictpins = {'1':1, '2':2, '3':3, '4':4, '17': 17}
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(dictpins[data['pin']], GPIO.OUT)
        pwm = GPIO.PWM(dictpins[data['pin']],50)
        pwm.start(0)
        pwm.ChangeDutyCycle(int(data['value']))
        time.sleep(0.2)
        pwm.stop()
        GPIO.cleanup()
        
    # if execute code
    if data['type'] == "execute":
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(17, GPIO.OUT)
        valueglob = data['value']
        globals()["blink"](data['value'])
        

        
sio.connect('http://172.20.10.4:5000/')
try:
    sio.sleep(1)
except KeyboardInterrupt:
    quit()

