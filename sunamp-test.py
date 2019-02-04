#!/usr/bin/python

import serial
# port on linux/mac devices can be found with 'ls /dev | grep -i usb'
# if you're on windows, god (google) help you (but it's probably one of COM0 to COM5)
port = '/dev/tty.usbserial-FTA636EW'
ser = serial.Serial(port, 9600, timeout=5) 

# last digit is checksum, checksum seems to be even/odd?
ser.write(bytearray([0x02, 0x67, 0x00, 0x00, 0x00, 0x00, 0x03, 0x00]))
# response to command
print(ser.read(8))
