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