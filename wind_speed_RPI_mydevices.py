#################################################################################################################
#Code to convert number of clicks to wind speed									#	
#Technique used here is simple 											#			
#Speed = Distance / time											#
#now here distance is Pie * r (where r is the radius i.e. from center of anemometer to the center of cup)	#
#In this anemometer, one click is caused when one cup of anemometer cover half the circumference, so when	#
#that click happen, we measure time taken 									#
#and divide the pie * r / time taken 										#	
#now when you use this code, please change .25 to the radius and that too in meter. 				#
################################################################################################################

import time
import datetime  
import RPi.GPIO as GPIO
import cayenne.client
GPIO.setmode(GPIO.BCM)  
  
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
count = 0
timestamp = 0
wind_km_float = 0
s_time = time.time()

#cayenne authentication info. This should be obtained from the Cayenne Dashboard.
MQTT_USERNAME  = "GET USERNAME FROM DASHBOARD"
MQTT_PASSWORD  = "GET PASSWORD FROM DASHBOARD"
MQTT_CLIENT_ID = "GET CLINET ID FROM DASHBOARD"

# The callback for when a message is received from Cayenne.
def on_message(message):
  print("message received: " + str(message))
  # If there is an error processing the message return an error string, otherwise return nothing.

client = cayenne.client.CayenneMQTTClient()
client.on_message = on_message
client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID)

i=0

def mine_callback_function(channel):
    global s_time
    time_now_in_callback = time.time()
    time_diff = time_now_in_callback - s_time
    wind_speed = .25 / time_diff
    wind_float = "%3.2f"% wind_speed #we are not assuming wind speed to be more than 999 km/hour i.e. 3 digit
    #convert wind speed from meter/hour to km/hour
    wind_km = float(wind_float) * 3.6
    global wind_km_float
    wind_km_float = "%3.2f"%wind_km
    print "wind speed in meter/hour is : {0} and in km/hour is : {1}".format(wind_float, wind_km_float)
    global count
    #print "falling edge detected on port 23,"  
    count = count + 1
    print "count before the time comparison  is {0}".format(count)
    s_time = time.time()

GPIO.add_event_detect(23, GPIO.FALLING, callback=mine_callback_function, bouncetime=200)  

def main(): 
	try:
	    while True:
		client.loop()
		global timestamp
		if (time.time() > timestamp + 10):
			client.windspeedWrite(1, wind_km_float)
			timestamp = time.time()
	except KeyboardInterrupt:  
	    GPIO.cleanup(23)       # clean up GPIO on CTRL+C exit  
	GPIO.cleanup()


if __name__ == "__main__":
	main() 
