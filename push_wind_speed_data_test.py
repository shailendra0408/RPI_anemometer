import cayenne.client
import time

# Cayenne authentication info. This should be obtained from the Cayenne Dashboard.
MQTT_USERNAME  = "USERNAME FROM DASHBOARD"
MQTT_PASSWORD  = "GET PASSWORD FROM DASHBOARD"
MQTT_CLIENT_ID = "GET CLIENT ID FROM DASHBOARD"

# The callback for when a message is received from Cayenne.
def on_message(message):
  print("message received: " + str(message))
  # If there is an error processing the message return an error string, otherwise return nothing.

client = cayenne.client.CayenneMQTTClient()
client.on_message = on_message
client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID)

i=22
timestamp = 0

while True:
  client.loop()

  if (time.time() > timestamp + 10):
        client.windspeedWrite(1, i)
        timestamp = time.time()
