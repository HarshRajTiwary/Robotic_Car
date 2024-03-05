from tkinter import *

import RPi.GPIO as GPIO
import time

root = Tk()
root.title("Remote Controle")
root.configure(bg='red')

GPIO.setmode(GPIO.BCM)

l = "" # for Memory

# Start Motor setup
a1 = 17
a2 = 27
b1 = 23
b2 = 24

GPIO.setup(a1, GPIO.OUT)
GPIO.setup(a2, GPIO.OUT)
GPIO.setup(b1, GPIO.OUT)
GPIO.setup(b2, GPIO.OUT)

def stop():
    GPIO.output(a1, GPIO.LOW)
    GPIO.output(a2, GPIO.LOW)
    GPIO.output(b1, GPIO.LOW)
    GPIO.output(b2, GPIO.LOW)

# End Motor setup

# Start Servo setup
servo_pin = 13
GPIO.setup(servo_pin, GPIO.OUT)
pwm = GPIO.PWM(servo_pin, 50)

def set_angle(angle):
    duty_cycle = (angle / 18) + 2
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(0.5)

pwm.start(0)


# set_angle(90)
# time.sleep(1)
# End Servo setup

# Start UltraSonic Setup

TRIG = 5
ECHO = 6
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def measure_distance():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()

    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    # Speed of sound = 343m/s = 34300cm/s
    # Distance = time * speed / 2 (since the sound wave travels to the object and back)
    distance = pulse_duration * 34300 / 2

    return distance

dist = measure_distance()
# time.sleep(0.1)
# end UltraSonic Setup

# Start IR Setup

ir_pin1 = 16
ir_pin1 = 25
GPIO.setup(ir_pin1, GPIO.IN)
GPIO.setup(ir_pin2, GPIO.IN)

ir_value1 = GPIO.input(ir_pin1)
ir_value2 = GPIO.input(ir_pin2)

# if ir_value1 == GPIO.HIGH:
#     print("Obstacle detected")

# end IR Setup


# Start Motor control
def forward():
    global l
    GPIO.output(a1, GPIO.HIGH)
    GPIO.output(b1, GPIO.HIGH)
    time.sleep(0.25)
    l = l+"f"
    stop()
    
def reverse():
    global l
    GPIO.output(a2, GPIO.HIGH)
    GPIO.output(b2, GPIO.HIGH)
    time.sleep(0.25)
    l = l+"b"
    stop()
    
def left():
    global l
    GPIO.output(a1, GPIO.HIGH)
    GPIO.output(b2, GPIO.HIGH)
    time.sleep(0.25)
    l = l+"l"
    stop()
    
def right():
    global l
    GPIO.output(a2, GPIO.HIGH)
    GPIO.output(b1, GPIO.HIGH)
    time.sleep(0.25)
    l = l+"r"
    stop()

# Start Motor control

def record():
    global l
    for i in l:
        if i=="l":
            left()
        elif i=="r":
            right()
        elif i=="f":
            forward()
        elif i=="b":
            reverse()
    l = ""

a = 15
b = 30

Button(root, text="Up", command=forward,height=a,width=b).grid(row=0, column=3)
Button(root, text="Right", command=right,height=a,width=b).grid(row=1, column=6)
Button(root, text="Left", command=left,height=a,width=b).grid(row=1, column=2)
Button(root, text="Down", command=reverse,height=a,width=b).grid(row=3, column=3)
Button(root, text="Repeat", command=record,height=5,width=30).grid(row=4, column=3)

mainloop()
pwm.stop()
GPIO.cleanup()