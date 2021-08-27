import RPi.GPIO as GPIO
import time
from yolo import YOLO

yolo = YOLO()

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

image = Image.open('./img/photo.jpg')
trash = yolo.out_predicted_class(self, image)

for i in trash:
    trash_class = trash[i]
    if(trash_class == 'can' or trash_class == 'plastic bottle'):
        GPIO.setup(21, RPi.GPIO.OUT)
        GPIO.output(channel, 1)
        time.sleep(2)
        GPIO.output(channel, 0)
        GPIO.cleanup()

    if(trash_class == 'fruit' or trash_class == 'vegetable'):
        GPIO.setup(22, RPi.GPIO.OUT)
        GPIO.output(channel, 1)
        time.sleep(2)
        GPIO.output(channel, 0)
        GPIO.cleanup()

    if(trash_class == 'battery'):
        GPIO.setup(23, RPi.GPIO.OUT)
        GPIO.output(channel, 1)
        time.sleep(2)
        GPIO.output(channel, 0)
        GPIO.cleanup()

    if(trash_class == 'china' or trash_class == 'cigarette'):
        GPIO.setup(24, RPi.GPIO.OUT)
        GPIO.output(channel, 1)
        time.sleep(2)
        GPIO.output(channel, 0)
        GPIO.cleanup()