from picamera import PiCamera
from time import sleep

myCamera = PiCamera()

myCamera.start_preview()

x = ['solarize', 'none', 'negative', 'film', 'emboss']

for effect in myCamera.IMAGE_EFFECTS:
    myCamera.image_effect = effect
    myCamera.annotate_text = "Effect: %s" % effect

    sleep(5)
   
    if effect in x:
    
        myCamera.capture("filename" + str(x.index(effect)) + ".jpg")

myCamera.stop_preview()
