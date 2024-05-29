# blinks the led

import serial
import time
arduino = serial.Serial(port="COM5", baudrate=9600)

x = 1
while True:
    data = str(x)
    data = data.encode()
    arduino.write(data)
    time.sleep(0.1) # blink interval 0.1 S
    if x == 1:
        x = 0
    elif x == 0:
        x = 1

