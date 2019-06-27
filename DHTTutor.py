import RPi.GPIO as GPIO
import dht11
import time
import datetime
import json
import requests

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 14
instance = dht11.DHT11(pin=4)

while True:
    result = instance.read()
    if result.is_valid():
        print("Last valid input: " + str(datetime.datetime.now()))
        print("Temperature: %d C" % result.temperature)
        print("Humidity: %d %%" % result.humidity)
    	data =data ='\r\n{\r\n  "m2m:cin": {\r\n    "cnf": "message",\r\n    "con": "\r\n      {\r\n      \t \\"Temperature\\": \\"'+str(result.temperature)+'\\",\r\n         \\"HUmidity\\": \\"'+str(result.humidity)+'\\"\r\n      }\r\n    "\r\n  }\r\n}'
	url = 'https://platform.antares.id:8443/~/antares-cse/antares-id/Monitoringsuhu/project1'
        headers = {'cache-control':'no-cache','content-type':'application/json;ty=4','x-m2m-origin':'784b5afbdb4dcf9c:5266aefaa9286a88'}
        r = requests.post(url,headers=headers,data=data)
    time.sleep(1)


