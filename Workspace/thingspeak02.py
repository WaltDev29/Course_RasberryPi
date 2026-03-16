import http.client
import urllib.request
import urllib.parse
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
        params = urllib.parse.urlencode({'field1': temperature, 'field2': humidity, 'field3': CdS, 'field4': GAS,  'key':key }) 
        headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = http.client.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            print(temperature, humidity, CdS, GAS)
            print(response.status, response.reason)
            data = response.read()
            conn.close()
            time.sleep(2)
            break
        except:
            print("connection failed")
if __name__ == "__main__":
    while True:
        thermometer()