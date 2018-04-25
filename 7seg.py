#! /usr/bin/python
#modified by DKing
#Finish 7segment code
import smbus
import time

#bus = smbus.SMBus(0)  # Rev 1 Pi uses 0
bus = smbus.SMBus(1)  # Rev 2 Pi uses 1


digit2sevenseg = [0x02, 0x9E, 0x24, 0x0C, 0x98, 0x48, 0xC0, 0x1E, 0x00, 0x18]

mcp2 = 0x22  # I2C address of MCP23017
bus.write_byte_data(0x22, 0x00, 0x00)  # Set all of bank A to outputs
time.sleep(1)

while True:
    for digit in range(0, 10):
        bus.write_byte_data(0x22, 0x14, 0x02)
        time.sleep(1)
        bus.write_byte_data(0x22, 0x14, 0x9E)
        time.sleep(1)
        bus.write_byte_data(0x22, 0x14, 0x24)
        time.sleep(1)
        bus.write_byte_data(0x22, 0x14, 0x0C)
        time.sleep(1)
        bus.write_byte_data(0x22, 0x14, 0x98)
        time.sleep(1)
        bus.write_byte_data(0x22, 0x14, 0x48)
        time.sleep(1)
        bus.write_byte_data(0x22, 0x14, 0xC0)
        time.sleep(1)
        bus.write_byte_data(0x22, 0x14, 0x1E)
        time.sleep(1)
        bus.write_byte_data(0x22, 0x14, 0x00)
        time.sleep(1)
        bus.write_byte_data(0x22, 0x14, 0x18)
        time.sleep(1)