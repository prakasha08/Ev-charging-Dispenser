import RPi.GPIO as GPIO
import time

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Set the GPIO pin to which the relay is connected (in this case, GPIO 18)
relay_pin = 23

# Set the GPIO pin as an output pin
GPIO.setup(relay_pin, GPIO.OUT)

try:
    while True:
        # Turn the relay on (close the switch)
        GPIO.output(relay_pin, GPIO.HIGH)
        print("Relay is ON")
          # Wait for 2 seconds

        # Turn the relay off (open the switch)
        # Wait for 2 seconds

except KeyboardInterrupt:
    GPIO.cleanup()


