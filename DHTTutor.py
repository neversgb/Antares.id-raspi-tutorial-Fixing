import RPi.GPIO as GPIO
import dht11
import time
import datetime
import request
import json

#initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

#read data using pin 4
instance = dht11.DHT11(pin=4)

while True:
result = instance.read()
if result.is_valid():
print("Last valid input: " + str(datetime.datetime.now()))
print("Temperature: %d C" % result.temperature)
print("Humidity: %d %%" % result.humidity)
data ='\r\n{\r\n  "m2m:cin": {\r\n    "cnf": "message",\r\n    "con": "\r\n      {\r\n      \t \\"status\\": \\"'+str(datetime.datetime.now())+'\\",\r\n         \\"dim\\": \\"10\\"\r\n      }\r\n    "\r\n  }\r\n}'
url = 'https://platform.antares.id:8443/~/antares-cse/antares-id/your-application-name/your-device-name'
headers = {'cache-control':'no-cache','content-type':'application/json;ty=4','x-m2m-origin':'Your-Acces-Key'}
r = request.post(url,headers=headers,data=data)
time.sleep(2)
							