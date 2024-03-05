import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
ir_pin = 17
GPIO.setup(ir_pin, GPIO.IN)

try:
    while True:
        ir_value = GPIO.input(ir_pin)

        if ir_value == GPIO.HIGH:
            print("Obstacle detected")
        else:
            print("No obstacle")

        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()
