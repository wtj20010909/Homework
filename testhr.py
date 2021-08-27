import sys
import RPi.GPIO as GPIO
import time

class hrsr04:
    def __init__(self):
        self.Trig_Pin = 17#引脚，BCM编号
        self.Echo_Pin = 27
    def inithr(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.Trig_Pin, GPIO.OUT, initial = GPIO.LOW)
        GPIO.setup(self.Echo_Pin, GPIO.IN)
        # time.sleep(2)

    def checkdist(self):
        GPIO.output(self.Trig_Pin, GPIO.HIGH)
        time.sleep(0.00015)
        GPIO.output(self.Trig_Pin, GPIO.LOW)
        while not GPIO.input(self.Echo_Pin):
            pass
        t1 = time.time()
        while GPIO.input(self.Echo_Pin):
            pass
        t2 = time.time()
        return (t2-t1)*340*100/2#返回距离值
