import RPi.GPIO as GPIO
import time

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Button pins
SW1_PIN = 4   # Forward
SW2_PIN = 17  # Reverse
SW3_PIN = 18  # Stop

# Motor pins
MOTOR_P = 19
MOTOR_M = 13

# Set up GPIO pins
GPIO.setup([SW1_PIN, SW2_PIN, SW3_PIN], GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup([MOTOR_P, MOTOR_M], GPIO.OUT)

def motor_forward():
    GPIO.output(MOTOR_P, GPIO.HIGH)
    GPIO.output(MOTOR_M, GPIO.LOW)
    print("Motor running forward")

def motor_reverse():
    GPIO.output(MOTOR_P, GPIO.LOW)
    GPIO.output(MOTOR_M, GPIO.HIGH)
    print("Motor running in reverse")

def motor_stop():
    GPIO.output(MOTOR_P, GPIO.LOW)
    GPIO.output(MOTOR_M, GPIO.LOW)
    print("Motor stopped")

try:
    while True:
        if GPIO.input(SW1_PIN) == GPIO.LOW:
            motor_forward()
        elif GPIO.input(SW2_PIN) == GPIO.LOW:
            motor_reverse()
        elif GPIO.input(SW3_PIN) == GPIO.LOW:
            motor_stop()
        
        time.sleep(0.1)  # Small delay to prevent button bouncing

except KeyboardInterrupt:
    GPIO.cleanup()