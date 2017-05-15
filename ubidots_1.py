#This code is provided by the Ubidots for sending one variable to Ubidots cluod  

from ubidots import ApiClient
import math
import time

# Create an ApiClient object

api = ApiClient(token='############################')

# Get a Ubidots Variable

variable = api.get_variable('##############################')

# Here is where you usually put the code to capture the data, either through your GPIO pins or as a calculation. We'll simply put an artificial signal here:

while(1):

    # Write the value to your variable in Ubidots
    response = variable.save_value({"value": 20*math.sin(10)})
    print response
    time.sleep(10)
