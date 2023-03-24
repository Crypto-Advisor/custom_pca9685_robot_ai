from flask import Flask
from flask_socketio import SocketIO, emit

import time
import keyboard
import board
import busio
from adafruit_pca9685 import PCA9685
from adafruit_motor import motor
from adafruit_servokit import ServoKit

# Initialize I2C bus and PCA9685 object
i2c = busio.I2C(board.SCL, board.SDA)
pca = PCA9685(i2c)
# Set PWM frequency to 1000Hz
pca.frequency = 60

# Set up PWM output on channel 0
motor_pwm = motor.DCMotor(pca.channels[1], pca.channels[1])

# Initialize the sero
kit=ServoKit(channels=16)

#FLASK APP
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route("/")
def ping():
    return 'RUNNING', 200


#WEBSOCKET ROUTES
@socketio.on('connect')
def test_connect():
    print('Client connected')
    
@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')

@socketio.on('control')
def handle_control(data):
    print('received control: ' + str(data))
    if data == 'forward':
        print('forward')
        motor_pwm.throttle = 0.1
    elif data == 'backward':
        print('backward')
        motor_pwm.throttle = -0.1
    elif data == 'right':
        print('right')
        kit.servo[0].angle = 180
    elif data == 'left':
        print('left')
        kit.servo[0].angle = 0
    elif data == 'reset-motor':
        motor_pwm.throttle = 0
        print('reset motor')
    elif data == 'reset-servo':
        kit.servo[0].angle = 90
        print('reset servo')
    else:
        print('invalid control')
        emit('invalid control', 'invalid control')


#HTTP ROUTES
@app.route("/forward")
def forward():
    try:
        print("forward")
        motor_pwm.throttle = 0.1
        return 'SUCCESS', 200
    except:
        return 'ERROR', 500
        
@app.route("/backward")
def backward():
    try:
        print("backward")
        motor_pwm.throttle = -0.1
        return 'SUCCESS', 200
    except:
        return 'ERROR', 500    
    
@app.route("/right")
def left():
    try:
        print("right")
        kit.servo[0].angle = 180
        return 'SUCCESS', 200
    except:
        return 'ERROR', 500


@app.route("/left")
def right():
    try:
        print("left")
        kit.servo[0].angle = 0
        return 'SUCCESS', 200
    except:
        return 'ERROR', 500
    

@app.route("/reset-motor")
def reset_motor():
    try:
        motor_pwm.throttle = 0
        print("reset motor")
    except:
        return 'ERROR', 500
    

@app.route("/reset-servo")
def reset_servo():
    try:
        kit.servo[0].angle = 90
        print("reset servo")
    except:
        return 'ERROR', 500
    
    

if __name__ == "__main__":
    # app.run(host='0.0.0.0')
    socketio.run(app, host='0.0.0.0')
