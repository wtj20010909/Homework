import cv2
from PIL import Image
from yolo import YOLO
import RPi.GPIO as GPIO

#physical_devices = tf.config.experimental.list_physical_devices('GPU')
#tf.config.experimental.set_memory_growth(physical_devices[0], True)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

image = Image.open('./img/photo.jpg')
trash = yolo.out_predicted_class(self, image)

yolo = YOLO()

def takephoto():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    resize = cv2.resize(frame, (416, 416), interpolation=cv2.INTER_NEAREST)
    cv2.imwrite('./img/photo.jpg', resize)
    try:
        image = Image.open('./img/photo.jpg')
    except:
        print('Open Error! Try Again!')
    else:
        trash = yolo.out_predicted_class(image)
        for i in trash:
            trash_class = trash[i]
            if (trash_class == 'can' or trash_class == 'plastic bottle'):
                GPIO.setup(21, RPi.GPIO.OUT)
                GPIO.output(channel, 1)
                time.sleep(2)
                GPIO.output(channel, 0)
                GPIO.cleanup()

            if (trash_class == 'fruit' or trash_class == 'vegetable'):
                GPIO.setup(22, RPi.GPIO.OUT)
                GPIO.output(channel, 1)
                time.sleep(2)
                GPIO.output(channel, 0)
                GPIO.cleanup()

            if (trash_class == 'battery'):
                GPIO.setup(23, RPi.GPIO.OUT)
                GPIO.output(channel, 1)
                time.sleep(2)
                GPIO.output(channel, 0)
                GPIO.cleanup()

            if (trash_class == 'china' or trash_class == 'cigarette'):
                GPIO.setup(24, RPi.GPIO.OUT)
                GPIO.output(channel, 1)
                time.sleep(2)
                GPIO.output(channel, 0)
                GPIO.cleanup()

    cap.release()
    cv2.destroyAllWindows()
    return 0

if __name__ == '__main__':
    takephoto()
