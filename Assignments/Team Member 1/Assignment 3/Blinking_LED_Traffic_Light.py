#Python Code for Blinking LED : 

import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) 
while True: 
    GPIO.output(8,GPIO.HIGH) 
    sleep(1) 
    GPIO.output(8,GPIO.LOW) 
    sleep(1)

#Python Code for Traffic Light: 

import RPi.GPIO as GPIO
import time 
try: 
    def trafficLight(led1, led2, led3, delay ): 
        GPIO.output(led1, 1)
        time.sleep(delay)
        GPIO.output(led1, 0) 
        GPIO.output(led2, 1) 
        time.sleep(delay) 
        GPIO.output(led2, 0) 
        GPIO.output(led3, 1)
        time.sleep(delay) 
        GPIO.output(led3, 0)
        GPIO.setmode(GPIO.BCM) 
        button = 19
        GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP) 
        ledGreen = 16
        ledYellow = 12 
        ledRed = 23 
        GPIO.setup(ledGreen, GPIO.OUT)
        GPIO.setup(ledYellow, GPIO.OUT) 
        GPIO.setup(ledRed, GPIO.OUT) 
    while True: 
        input_state = GPIO.input(button) 
        if input_state == False: 
            print('Button Pressed') 
            trafficLight(ledGreen, ledYellow, ledRed, 1) 
        else: 
            GPIO.output(ledGreen, 0) 
            GPIO.output(ledYellow, 0) 
            GPIO.output(ledRed, 0)
except KeyboardInterrupt:
    print "You have exited the Program" 
finally: 
    GPIO.cleanup()
