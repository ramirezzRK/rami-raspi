#!/usr/bin/python

import smbus
import pdb
import time

class DS3231temp:
## Initialize I2C Interface
	def __init__(self, address=0x68, busnum=-1):
		self.address = address
		self.bus = smbus.SMBus(1)

	def errMsg(self):
		print "Error accessing 0x%02X: Check your I2C address" % self.address
		return -1

	def readByteData(self, register):
		try:
			results = self.bus.read_byte_data(self.address, register)
			return results
		except IOError, err:
			return self.errMsg()	
	
	def writeByteData(self, register, value):
		try: 
			self.bus.write_byte_data(self.address, register, value)
		except IOError, err:
			return self.errMsg()
	
	def readTemp(self):
		self.writeByteData(0x0E, 0x3C) # tells controller to update temperature readings
		INtemp = self.readByteData(0x11) # reads integer part of the temperature
		FLtemp = self.readByteData(0x12) # reads float part of temperature
		temperature = (((INtemp << 8) | FLtemp) >> 6) / 4.0 # join temperatures together
		return temperature
		
skuska = DS3231temp(0x68)
print(skuska.readTemp())

