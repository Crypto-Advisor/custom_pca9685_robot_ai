from tkinter import *

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

def turn_left(event):
    print("left")
    kit.servo[0].angle = 180
    
def turn_right(event):
    print("right")
    kit.servo[0].angle = 0
    
def forward(event):
    print("forward")
    motor_pwm.throttle = 0.1
    
def backward(event):
    print("backward")
    motor_pwm.throttle = -0.1
    
def reset_motor(event):
    motor_pwm.throttle = 0
    print("reset motor")
    
def reset_servo(event):
    kit.servo[0].angle = 90
    print("reset servo")


root = Tk()  # create parent window

forward_button = Label(root, text="Forward")
forward_button.pack(pady=10, padx=10)

backward_button = Label(root, text="Backward")
backward_button.pack(pady=10, padx=10)

left_button = Label(root, text="Left")
left_button.pack(pady=10, padx=10)

right_button = Label(root, text="Right")
right_button.pack(pady=10, padx=10)

forward_button.bind("<Button-1>", forward)
forward_button.bind("<ButtonRelease-1>", reset_motor)

backward_button.bind("<Button-1>", backward)
backward_button.bind("<ButtonRelease-1>", reset_motor)

left_button.bind("<Button-1>", turn_left)
left_button.bind("<ButtonRelease-1>", reset_servo)

right_button.bind("<Button-1>", turn_right)
right_button.bind("<ButtonRelease-1>", reset_servo)

root.mainloop()