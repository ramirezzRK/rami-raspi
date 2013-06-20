Couple of libraries if you are just starting with raspberry pi and python

DS3231temp.py - reads temperature from real time clock DS3231, note that it has steps of 0.25 C.
		usage : import DS3231temp
			test = DS3231temp(0x68) # add your device address, you can check it in 
						# i2cdev -y 1 (if 512MB pi) i2cdev -y 0 (if 256MB pi)
						# how to install i2c tools and make it work please refer to 
						# the great adafruit tutorial: 	goo.gl/EPcs9
			print(test())
