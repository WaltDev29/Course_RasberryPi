import urllib.request
import Adafruit_DHT
import time
from i2c_class import read_i2c
 
key = "L3E180S9BHW4K66B"  # Put your API Key here
sensor = Adafruit_DHT.DHT11
pin = 27
adc = read_i2c()
 
def thermometer():
    while True:
        humidity, temperature = Adafruit_DHT.read(sensor, pin)
        CdS = adc.cds_read()
        GAS = adc.gas_read()
        url = 'https://api.thingspeak.com/update'
        url = url +'?api_key=%s'%key
        url = url + '&field1=%s'%temperature
        url = url + '&field2=%s'%humidity
        url = url + '&field3=%s'%CdS
        url = url + '&field4=%s'%GAS
        try:
            urllib.request.urlopen(url)
            time.sleep(0.5)
            break
        except:
            print("connection failed")
            
if __name__ == "__main__":
        while True:
                thermometer()
