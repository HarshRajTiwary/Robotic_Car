import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
TRIG = 18
ECHO = 24

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

try:
    while True:
        dist = measure_distance()
        print("Distance: {:.2f} cm".format(dist))
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()