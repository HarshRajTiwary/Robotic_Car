import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
servo_pin = 18
GPIO.setup(servo_pin, GPIO.OUT)
pwm = GPIO.PWM(servo_pin, 50)

def set_angle(angle):
    duty_cycle = (angle / 18) + 2
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(0.5)

pwm.start(0)

try:
    while True:
        set_angle(0)
        time.sleep(1)

        set_angle(90)
        time.sleep(1)

        set_angle(180)
        time.sleep(1)

except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
