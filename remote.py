from tkinter import *

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

l = ""

a1 = 17
a2 = 27
b1 = 23
b2 = 24

GPIO.setup(a1, GPIO.OUT)
GPIO.setup(a2, GPIO.OUT)
GPIO.setup(b1, GPIO.OUT)
GPIO.setup(b2, GPIO.OUT)


def new():
    GPIO.output(a1, GPIO.LOW)
    GPIO.output(a2, GPIO.LOW)
    GPIO.output(b1, GPIO.LOW)
    GPIO.output(b2, GPIO.LOW)


root = Tk()
root.title("Remote Controle")
root.configure(bg='red')

def forward():
    global l
    GPIO.output(a1, GPIO.HIGH)
    GPIO.output(b1, GPIO.HIGH)
    time.sleep(0.25)
    l = l+"f"
    new()
    
def reverse():
    global l
    GPIO.output(a2, GPIO.HIGH)
    GPIO.output(b2, GPIO.HIGH)
    time.sleep(0.25)
    l = l+"b"
    new()
    
def left():
    global l
    GPIO.output(a1, GPIO.HIGH)
    GPIO.output(b2, GPIO.HIGH)
    time.sleep(0.25)
    l = l+"l"
    new()
    
def right():
    global l
    GPIO.output(a2, GPIO.HIGH)
    GPIO.output(b1, GPIO.HIGH)
    time.sleep(0.25)
    l = l+"r"
    new()
    
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
GPIO.cleanup()