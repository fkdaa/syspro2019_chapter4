import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
servo = GPIO.PWM(2, 50)
servo.start(0.0)

n = 1900/180

def setservo(dig):
	buf = 1440.0
	if dig!=0:
		buf += dig*n
	buf = buf/20000.0*100
	print(buf)
	servo.ChangeDutyCycle(buf)

for i in range(-3,4):
	setservo(i*30)
	time.sleep(1.0)

GPIO.cleanup()


