#import required libraries
import serial
import struct
#from visual import *
#import numpy as np
 
#Start the serial port to communicate with arduino
data = serial.Serial('/dev/ttyACM1',9600, timeout=1)
 
'''
#Create virtual environment:
#first we create the arrow to show current position of the servo
measuringArrow = arrow(pos=(0,-10,0), axis=(0,10,0), shaftwidth=0.4, headwidth=0.6)
#and the now the labels
angleLabel = label (text = 'Servo angle is: 90', pos=(0,5,0), height=15, box=false)
angle0 = label (text = '0', pos=(-10,-10,0), height=15, box=false)
angle45 = label (text = '45', pos=(-7.5,-2.5,0), height=15, box=false)
angle90 = label (text = '90', pos=(0,1,0), height=15, box=false)
angle135 = label (text = '135', pos=(7.5,-2.5,0), height=15, box=false)
angle180 = label (text = '180', pos=(10,-10,0), height=15, box=false)
'''


#now we made an infinite while loop to keep the program running
#while (1==1):
  	#rate(20) #refresh rate required for VPython
  	#pos = input("Enter a number: ") #Prompt the user for the angle
  	#myLabel = 'Servo angle is: '+str(pos) #update the text of the label for the virtual environment
pos=50;
data.write(struct.pack('>B',pos)) #code and send the angle to the Arduino through serial port
	#angleLabel.text = myLabel #refresh label on virtual environment
	#measuringArrow.axis=(-10*np.cos(pos*0.01745),10*np.sin(pos*0.01745),0) #calculate the new axis of the indicator
