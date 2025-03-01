# Create the ADS object
ads = ADS.ADS1015(i2c, address=adrs)  # Use the correct I2C address

# Set the gain (if needed)
ads.gain = 2 / 3  # This corresponds to a range of +/- 6.144V

# Assign the analog input channel (0, 1, 2, or 3)
chan = AnalogIn(ads, ADS.P1)  # Use the correct AIN pin
n = 5
sum = 0
surface_ref = lambda x, y: x - 50 < y < x + 50
# x is the l[0] or l[1].. and y is value to be checked
ref_dict = {"oil": 234, "plain": 2356, "marble": 767, "water": 2345}
try:
    while n:
        tcrt_value = chan.value  # Read the TCRT5000 value
        sum += tcrt_value
        n -= 1
        time.sleep(0.1)
        # You can convert the TCRT5000 value to distance or reflectivity as needed
    else:
        for i in ref_dict.keys():
            if surface_ref(ref_dict[i], sum // 5):
                speak_text(f"flooris {ref_dict.keys[i]}")

except KeyboardInterrupt:
    pass

def sonic_distance():
    try:
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        while GPIO.input(ECHO) == 0:
            pulse_start = time.time()

        while GPIO.input(ECHO) == 1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        return distance

    except KeyboardInterrupt:
        GPIO.cleanup()


def obstacleDetect():
    # Read the value coming from Analogue In Pin 0, set gain to the above value

    # Perform distance measurement with the ultrasonic sensor
    pwm = GPIO.PWM(SERVO_PIN, 60)
    pwm.start(7.5)

    for angle in [0, 45, 90, 135, 180]:
        rotate_servo(angle, pwm)
        dist = sonic_distance()

        if dist < 200:
            speak_text(f"Obj{angle} ")

    ▋