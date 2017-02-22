#!/usr/bin/python
import yaml
from firebase import firebase
import serial
import time
import json

config = yaml.safe_load(open("./../config.yml"))

firebaseConnection = firebase.FirebaseApplication(config['firebase']['url'])

print "AQUAPILOT";
arduinoSerial = serial.Serial('/dev/ttyACM0', 9600)

while 1 :
    arduinoMsg = arduinoSerial.readline()
    print ">> " + arduinoMsg
    try:
        msg = json.loads(arduinoMsg)
        msg['timestamp'] = time.time()
        firebaseConnection.post('/measures/'+msg['label']+'/'+msg['sensor'], msg)
    except (ValueError, KeyError, TypeError):
        print "JSON format error : " + arduinoMsg