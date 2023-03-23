from django.http import HttpResponse

# imports for app
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

def turn_left():
    kit.servo[0].angle = 180
    
def turn_right():
    kit.servo[0].angle = 0
    
def forward():
    motor_pwm.throttle = 0.1
    
def backward():
    motor_pwm.throttle = -0.1


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")