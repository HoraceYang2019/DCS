'''
-----------------------------------------------------------------------
for Rasbian: 
 wget http://repo.mosquitto.org/debian/mosquitto-repo.gpg.key
 sudo apt-key add mosquitto-repo.gpg.key
 rm mosquitto-repo.gpg.key
 cd /etc/apt/sources.list.d/
 sudo wget  http://repo.mosquitto.org/debian/mosquitto-jessie.list
 sudo apt-get update
 sudo apt-get upgrade
 sudo apt-get dist-upgrade
 sudo apt-get install mosquitto mosquitto-clients
 service mosquitto status
 
 sudo pip3 install paho-mqtt

Ref: http://cheng-min-i-taiwan.blogspot.tw/2015/03/raspberry-pimqtt-android.html
-----------------------------------------------------------------------
for Windows:
 pip install paho-mqtt

-----------------------------------------------------------------------
@author: Horace
'''

# Subscriber.py
import paho.mqtt.subscribe as subscribe

host = "iot.eclipse.org"
portNo = 	1883

def on_message_print(client, userdata, message):
    print("%s %s" % (message.topic, message.payload))

# In[]
# Test 1: start first to subscribe mqtt message by "mislab/mqtt/msg" 
    
msg = subscribe.simple("mislab/mqtt/xyz", hostname=host)
print("I got mqtt: %s with %s" % (msg.topic, msg.payload))

# In[]
# Test 2: start first to subscribe mqtt message by "mislab/mqtt/callback" without stop

subscribe.callback(on_message_print, "mislab/mqtt/xyz", hostname=host)

# In[]
# Test 3: start first to subscribe mqtt message by "mislab/mqtt/multiple" without stop

subscribe.callback(on_message_print, "mislab/mqtt/multiple", hostname=host)

# In[]
# Test 4: use another MQTT Server

host = "m14.cloudmqtt.com" 
portNo = 	17640 
authpass = {'username':"vfhmwuwd", 'password':"9Na3SdDn7KvW"}
subscribe.callback(on_message_print, "mislab/mqtt/cloudmqtt", hostname=host, port = portNo, auth = authpass)