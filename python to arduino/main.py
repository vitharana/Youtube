# sending data by the keyboard to control the led 
# 1 - led on
# 0 - led off

import serial

arduino = serial.Serial(port="COM5", baudrate=9600)

while True:
    data = input("Enter the number :")
    data = data.encode()
    arduino.write(data)
