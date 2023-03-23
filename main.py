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


def main():
    print('STARTING!')
    
    while True:
        if keyboard.is_pressed('w'):
            while keyboard.is_pressed('w'):
                print('forward')
                forward()
            #default motor speed
            print('Default')
            motor_pwm.throttle = 0
            
        elif keyboard.is_pressed('s'):
            while keyboard.is_pressed('s'):
                print('backward')
                backward()
            #default motor speed
            print('Default')
            motor_pwm.throttle = 0
        
        if keyboard.is_pressed('a'):
            while keyboard.is_pressed('a'):
                print('left')
                turn_left()
            #default servo position
            print('Default')
            kit.servo[0].angle = 90
            
        elif keyboard.is_pressed('d'):
            while keyboard.is_pressed('d'):
                print('right')
                turn_right()
            #default servo position
            print('Default')
            kit.servo[0].angle = 90
            
        if keyboard.is_pressed('q'):
            break
    
    print('STOPPING!')
    pca.deinit()
    
main()