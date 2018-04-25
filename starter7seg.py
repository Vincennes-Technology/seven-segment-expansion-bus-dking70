#! /usr/bin/python
import smbus
import time

#bus = smbus.SMBus(0)  # Rev 1 Pi uses 0
bus = smbus.SMBus(1) # Rev 2 Pi uses 1


mcp2 = 0x22

#These constants were derived from the data sheet
IODIRA = 0x00 # Pin direction register
IODIRB = 0x01
OLATA  = 0x14 # Register for outputs
OLATB = 0x15
digit2sevenseg=[0xc0,0xf9,0xa4,0xb0,0x99,0x92,0x83,0xf8,0x80,0x98]

# Set all GPA pins as outputs by setting
# all bits of IODIRA register to 0

bus.write_byte_data(mcp2,IODIRA,0x00)
bus.write_byte_data(mcp2,IODIRB,0x00)

# Set output all 7 output bits to 0

bus.write_byte_data(mcp2,OLATA,0xff)
bus.write_byte_data(mcp2,OLATB,0xff)


def countupdigit(device,port):
    for MyData in range(0,10):
      # Count from 0 to 10 which in binary will count
      bus.write_byte_data(device,port,digit2sevenseg[MyData])
      time.sleep(1)

    # Set all bits to zero
    #bus.write_byte_data(DEVICE,OLATA,0)

countupdigit(mcp2,1)

