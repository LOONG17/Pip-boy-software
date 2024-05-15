import RPi.GPIO as GPIO
from time import sleep

# Define GPIO pins
CLK_PIN = 18
DT_PIN = 17
SW_PIN = 27

# Set GPIO mode
GPIO.setmode(GPIO.BCM)

# Set up GPIO pins
GPIO.setup(CLK_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(DT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SW_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Define a callback function for the encoder
def rotary_callback(channel):
    global counter
    if GPIO.input(DT_PIN):
        counter += 1
        print("Encoder twisted clockwise")
    else:
        counter -= 1
        print("Encoder twisted counter-clockwise")
    print("Counter:", counter)

# Define a callback function for the switch
def switch_callback(channel):
    print("Switch pressed")

# Add event detection to the CLK_PIN and SW_PIN
GPIO.add_event_detect(CLK_PIN, GPIO.RISING, callback=rotary_callback)
GPIO.add_event_detect(SW_PIN, GPIO.FALLING, callback=switch_callback, bouncetime=300)

# Initialize counter variable
counter = 0

try:
    while True:
        sleep(0.1)  # Sleep to reduce CPU usage

except KeyboardInterrupt:
    GPIO.cleanup()  # Clean up GPIO on CTRL+C exit
