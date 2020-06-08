import time
import sys
import random
import ibmiotf.application
import ibmiotf.device

#Provide your IBM Watson Device Credentials
organization = "cp7nel" # repalce it with organization ID
deviceType = "project" #replace it with device type
deviceId = "1234" #repalce with device id
authMethod = "token"
authToken = "1234567890"#repalce with token

def myCommandCallback(cmd):
        print("Command received: %s" % cmd.data)        
        if cmd.data['command']=='submit':
                print("The readings are ")
                
try:
    deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
    deviceCli = ibmiotf.device.Client(deviceOptions)
    #..............................................
    
except Exception as e:
    print("Caught exception connecting device: %s" % str(e))
    sys.exit()
deviceCli.connect()
while True:
        Temp =round(random.uniform(0,41) ,1)
        systolic =random.randint(60,162)
        diastolic=random.randint(40,102)
        pulse = random.randint(30,180)
        age = random.randint(0,60)
        
        
        
        
        data = {'d':{'Age':age, 'Temperature' : Temp, 'Systolic': systolic, 'Diastolic':diastolic, 'Pulse': pulse  }}
        #print data
        def myOnPublishCallback():
            print ("Age =%s " %age , "Temperature = %s C" % Temp, "Systolic = %s " % systolic,"Diastolic = %s " % diastolic, "Pulse = %s " % pulse, "to IBM Watson")
        success = deviceCli.publishEvent("event", "json", data, qos=0, on_publish=myOnPublishCallback)
        if not success:
            print("Not connected to IoTF")
        time.sleep(5)
        
        
# Disconnect the device and application from the cloud
deviceCli.disconnect()
