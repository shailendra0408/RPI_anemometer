###This code contain two important parts

1. Getting data from a Anemometer with two wires on a RPI using interrupt (RPI.GPIO).

2. Pushing data to a IOT cloud 
    1. Cayenne MQTT cloud 
    2. Ubidots IOT cloud with 5000 free credits
    3. I will be adding some sample code for other cloud soon.  
 

#Getting data from a anemometer 
1. Anemometer is a device which measure wind speed. Working in my present IOT startup, gave me lot of chances to work around weather sensors like Temperature, Humidity, Pressure, Wind speed, wind direction and many others. Although all that code we in the team wrote was on microcontrollers where accessing low level pheripherals is relatvively easy when you compare to a machine running linux. You have to anyhow depend on the libraries, because Linux kernel donot allow you to mangle up with the low level pheripherals but any how probably some time i will give it a try.
 
2. I user RPI.GPIO module and there were lot of example available in thr rich community of RPI. So i used one of them. This was easy. 

3. Now to convert number of pulses in wind speed was a bit tricky. Then i remembered my colleauge statement and then it become clear. Its simple 
```speed = Distance / time.
```
 I had expalined more about it in the code itself. 


#Getting data posted to a MQTT cloud - Cayenne My devices MQTT cluod - https://mydevices.com/

1. First of all, they had pusblished a python library - Here is the (LINK) (https://github.com/myDevicesIoT/Cayenne-MQTT-Python)

2. In their sample program, they give you only ceratin function to push data for ceratin sensor. So i made a small change in the client.py file which is in 
```    1. /usr/local/lib/python2.7/dist-packages/cayenne
```
    2. Use sudo to edit the file 

    3. added one more function of windspeedWrite. I took help of previous functions and this [LINK] ( https://mydevices.com/cayenne/docs/#bring-your-own-thing-api-supported-data-types) supported data type section 

3. And then it was plain easy. 


#Cayenne MQTT cloud 

1. While pushing data to cloud, this error keep on coming and i donot have a f_____g clue that what is the reason

Disconnected with result code 1

Disconnected with result code 1

2. In their dashboard, no matter how much data you send, Graph will show - no data available with a date of Jan1, 5.30 AM and today is 13th May 2017. 
3. Dahsboard is f_____g slow. Although i admire that they provide this kind of functionality for free and you call me greedy. 

Ubidots IOT cloud
1. Pushing data to Ubidots cluod turn out to be too simple. You can either send one variable or multiple variable. 
2. They have a Python module using which you can send data to cloud easily. You will require your API token which you can get from your account [LINK] ( https://ubidots.com/docs/index.html#send-one-value-to-ubidots) 
  
3. Here is the link for the python documentation i used [LINK] (http://help.ubidots.com/connect-your-devices/connect-the-raspberry-pi-with-ubidots)
    



