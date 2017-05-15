from ubidots import ApiClient
import random
import time 
objectapi = ApiClient(token='ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZzzzzZZz')
while 1:
    objectapi.save_collection([
      {'variable': '5919fed37625423e468a7e74', 'value': random.random()}, 
      {'variable': '5919fee37625423e468a7fa4', 'value': random.random()},
      {'variable': '5919feef7625423e468a80a5', 'value': random.random()},
      {'variable': '5919fefd7625423e468a81e2', 'value': random.random()}
    ])
    print "going to sleep after pushing data to cloud"
    time.sleep(10)
