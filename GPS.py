def gpio_spinleft():
    GPIO.output(yellow, GPIO.LOW)
    GPIO.output(green, GPIO.HIGH)
    GPIO.output(blue, GPIO.LOW)
    GPIO.output(white, GPIO.HIGH)
    print('左方')

def gpio_spinright():
    GPIO.output(yellow, GPIO.HIGH)
    GPIO.output(green, GPIO.LOW)
    GPIO.output(blue, GPIO.HIGH)
    GPIO.output(white, GPIO.LOW)
    print('右方')

def gpio_stop():
    GPIO.output(yellow, GPIO.LOW)
    GPIO.output(green, GPIO.LOW)
    GPIO.output(blue, GPIO.LOW)
    GPIO.output(white, GPIO.LOW)
    print('停止')

def gpio_goback():
    GPIO.output(yellow, GPIO.HIGH)
    GPIO.output(green, GPIO.LOW)
    GPIO.output(blue, GPIO.LOW)
    GPIO.output(white, GPIO.HIGH)
    print('後方')

def ultrasonic_distance():
    time.sleep(0.1)
    GPIO.output(trigger, 1)
    time.sleep(0.00001)
    GPIO.output(trigger, 0)
    while GPIO.input(echo) == 0:
        pass
    ultrasonic_start = time.time()
    while GPIO.input(echo) == 1:
        pass
    ultrasonic_stop = time.time()
    timed = (ultrasonic_stop - ultrasonic_start) / 2
    distance = timed * 34300
    return distance

def servo(angle):
    if angle == '180':
        GPIO.output(servo180, GPIO.HIGH)
        print('180')
        time.sleep(0.5)

    if angle == 'left':
        GPIO.output(servo_left, GPIO.HIGH)
        print('left')
        time.sleep(0.5)

    if angle == 'right':
        GPIO.output(servo_right, GPIO.HIGH)
        print('right')
        time.sleep(0.5)

    if angle == '0':
        GPIO.output(servo0, GPIO.HIGH)
        print('0')
        time.sleep(0.5)

def servo_return():
    GPIO.output(servo180, GPIO.LOW)
    GPIO.output(servo_left, GPIO.LOW)
    GPIO.output(servo_right, GPIO.LOW)
    GPIO.output(servo0, GPIO.LOW)

def LCD_setup():
    bus = smbus.SMBus(1)
    time.sleep(0.1)
    bus.write_i2c_block_data(0x3e, 0x00, [0x38, 0x39, 0x14, 0x70, 0x56, 0x6c])
    time.sleep(0.3)

import RPi.GPIO as GPIO
import time
import smbus

# GPIO pin constants
YELLOW_PIN = 17
GREEN_PIN = 18
BLUE_PIN = 27
WHITE_PIN = 22
TRIGGER_PIN = 23
ECHO_PIN = 24
SERVO_180_PIN = 25
SERVO_LEFT_PIN = 5
SERVO_RIGHT_PIN = 6
SERVO_0_PIN = 12

def gpio_setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup([YELLOW_PIN, GREEN_PIN, BLUE_PIN, WHITE_PIN, TRIGGER_PIN, SERVO_180_PIN, SERVO_LEFT_PIN, SERVO_RIGHT_PIN, SERVO_0_PIN], GPIO.OUT)
    GPIO.setup(ECHO_PIN, GPIO.IN)

def gpio_spinleft():
    """Spin to the left."""
    GPIO.output(YELLOW_PIN, GPIO.LOW)
    GPIO.output(GREEN_PIN, GPIO.HIGH)
    GPIO.output(BLUE_PIN, GPIO.LOW)
    GPIO.output(WHITE_PIN, GPIO.HIGH)
    print('左方')

def gpio_spinright():
    """Spin to the right."""
    GPIO.output(YELLOW_PIN, GPIO.HIGH)
    GPIO.output(GREEN_PIN, GPIO.LOW)
    GPIO.output(BLUE_PIN, GPIO.HIGH)
    GPIO.output(WHITE_PIN, GPIO.LOW)
    print('右方')

def gpio_stop():
    """Stop all movement."""
    GPIO.output(YELLOW_PIN, GPIO.LOW)
    GPIO.output(GREEN_PIN, GPIO.LOW)
    GPIO.output(BLUE_PIN, GPIO.LOW)
    GPIO.output(WHITE_PIN, GPIO.LOW)
    print('停止')

def gpio_goback():
    """Move backward."""
    GPIO.output(YELLOW_PIN, GPIO.HIGH)
    GPIO.output(GREEN_PIN, GPIO.LOW)
    GPIO.output(BLUE_PIN, GPIO.LOW)
    GPIO.output(WHITE_PIN, GPIO.HIGH)
    print('後方')

def ultrasonic_distance():
    """Measure distance using ultrasonic sensor."""
    time.sleep(0.1)
    GPIO.output(TRIGGER_PIN, 1)
    time.sleep(0.00001)
    GPIO.output(TRIGGER_PIN, 0)
    while GPIO.input(ECHO_PIN) == 0:
        pass
    ultrasonic_start = time.time()
    while GPIO.input(ECHO_PIN) == 1:
        pass
    ultrasonic_stop = time.time()
    timed = (ultrasonic_stop - ultrasonic_start) / 2
    distance = timed * 34300
    return distance

def servo(angle):
    """Control servo motor based on the given angle."""
    angle_pins = {
        '180': SERVO_180_PIN,
        'left': SERVO_LEFT_PIN,
        'right': SERVO_RIGHT_PIN,
        '0': SERVO_0_PIN
    }
    if angle in angle_pins:
        GPIO.output(angle_pins[angle], GPIO.HIGH)
        print(angle)
        time.sleep(0.5)
    else:
        print('Invalid angle')

def servo_return():
    """Return servo to the base position."""
    GPIO.output(SERVO_180_PIN, GPIO.LOW)
    GPIO.output(SERVO_LEFT_PIN, GPIO.LOW)
    GPIO.output(SERVO_RIGHT_PIN, GPIO.LOW)
    GPIO.output(SERVO_0_PIN, GPIO.LOW)

def LCD_setup():
    """Setup LCD display."""
    bus = smbus.SMBus(1)
    time.sleep(0.1)
    bus.write_i2c_block_data(0x3e, 0x00, [0x38, 0x39, 0x14, 0x70, 0x56, 0x6c])
    time.sleep(0.3)

if __name__ == "__main__":
    try:
        gpio_setup()
        # Add your main logic here
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        GPIO.cleanup()
