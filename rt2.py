from KY040 import KY040
import os, time
 
 
def readVolume():
    value = os.popen("amixer get PCM|grep -o [0-9]*%|sed 's/%//'").read()
    return int(value)
def rotaryChange(direction):
    volume_step = 5
    volume = readVolume()
    if direction == 1:
        os.system("sudo amixer set PCM -- "+str(min(100,max(0,volume + volume_step)))+"%")
    else:
        os.system("sudo amixer set PCM -- "+str(min(100,max(0,volume - volume_step)))+"%")
def switchPressed():
     print "button pressed"
 
 
if __name__ == "__main__":
 
    CLOCKPIN = 5
    DATAPIN = 6
    SWITCHPIN = 13
  
    
    GPIO.setmode(GPIO.BCM)
    
    ky040 = KY040(CLOCKPIN, DATAPIN, SWITCHPIN, rotaryChange, switchPressed)
 
    ky040.start()
 
    try:
        while True:
            time.sleep(0.05)
    finally:
        ky040.stop()
        GPIO.cleanup()
 
