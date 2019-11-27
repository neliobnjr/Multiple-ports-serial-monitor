import serial
from time import sleep
from time import time, strftime, localtime
import sys

COM5 = 'COM5'
COM3 = 'COM3'# /dev/ttyACM0 (Linux)
BAUD = 9600

ser5 = serial.Serial(COM5, BAUD, timeout = .1)
ser = serial.Serial(COM3, BAUD, timeout = .1)

file_name = 'vacdata.csv'
print('Waiting for device');
f = open(file_name, 'w+')
f.write("time,Right side plate,Left side plate,Environment temp,Pressure,Humidity,Gauge Pressure\n")
sleep(1)
print(ser.name)
print(ser5.name)

#check args
if("-m" in sys.argv or "--monitor" in sys.argv):
	monitor = True
else:
	monitor= False

while True:
	val = str(ser.readline().decode().strip(' \r\n'))#Capture serial output as a decoded string
	#valwrite = ("p")
	val1 = ('p'.encode())
	ser5.write(val1)
	val2 = str(ser5.readline(10).decode().strip(' \r\n'))
	#valA = val.split(" \n")
	#print()
	if(monitor == True):
		print(val+','+val2)
		print('\n')
		f.write(strftime("%H:%M:%S,", localtime()) + val +','+ val2 + "\n")

		sleep(1)


  # open file in append mode

f.close()
