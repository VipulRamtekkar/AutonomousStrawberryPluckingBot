#Code for the autonomous strawberry plucking bot
import cv2
import numpy as np
import time
import math
import detection
import serial
import RPi.GPIO as GPIO
import picamera 
import detection
#Initializing the picamera 
camera = picamera.PiCamera() 

#The serial port which is connected to the arduino so that data can 
#read and written from it
arduino_arm = serial.Serial('/dev/ttyACM1',9600)
stepper = serial.Serial('/dev/ttyACM0',9600)

def arm():
	arduino_arm.write('3')

def startcam():
	camera.start_preview()
	time.sleep(1)

def captureImg():                                                           
	camera.capture('runimg.jpg')
	img = cv2.imread('runimg.jpg', 1)
	return img

def stopCam():                                                             
	camera.stop_preview()

def Stepper():
	stepper.write('30')
'''
def calcenter(contour):
	cv2.moments(contour) #gives the information about centroid, moi, etc.
	cx = int(M['m10']/M['m00'])
	cy = int(M['m01']/M['m00'])
	center=(cx,cy)
	return center
'''
# initializing the camera 

if __name__=="__main__":

	start_time = time.time()
	startcam()         # the stains code patch will run for about 420 seconds and then the second patch will start 

	while ((time.time()-start_time) < 4200):
		im = captureImg()
		im = cv2.imread(im)
		a = detection.find_strawberry(im)

		if (a == 0):
			#Rotate the stepper
			print (a)
			Stepper()
			#print (" rotate the stepper")

		if (a==1):
			print (a)
			#print ("The detected contour is a strawberry")
			arm()
			#Perform grab operation
	stopCam()



















