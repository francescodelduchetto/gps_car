
# import threading
import RPi.GPIO as GPIO

class Buttons():
    def __init__(self, on_green, on_blue, on_red):
        super(Buttons, self).__init__()

        #Set the Buttons and LED pins
        self.greenButton = 23
        self.greenLED = 24

        self.redButton = 16
        self.redLED = 13

        self.blueButton = 27
        self.blueLED = 4
        
        GPIO.output(self.greenLED, False)
        GPIO.output(self.blueLED, False)
        GPIO.output(self.redLED, False)

        #Set warnings off (optional)
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.cleanup()

        #Setup the Buttons and LEDs
        GPIO.setup(self.greenButton,GPIO.IN,pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.greenLED,GPIO.OUT)

        GPIO.setup(self.redButton,GPIO.IN,pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.redLED,GPIO.OUT)

        GPIO.setup(self.blueButton,GPIO.IN,pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.blueLED,GPIO.OUT)

        GPIO.add_event_detect(self.greenButton, GPIO.RISING, callback=on_green, bouncetime=1100)
        GPIO.add_event_detect(self.redButton, GPIO.FALLING, callback=on_red, bouncetime=1100)
        GPIO.add_event_detect(self.blueButton, GPIO.FALLING, callback=on_blue, bouncetime=1100)
        
    def setGreenLed(self, value):
        GPIO.output(self.greenLED, value)
    
    def setRedLed(self, value):
        GPIO.output(self.redLED, value)
    
    def setBlueLed(self, value):
        GPIO.output(self.blueLED, value)

    def cleanup(self):
        GPIO.cleanup()


