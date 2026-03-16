import Adafruit_DHT
import time

# DHT11 센서 객체를 선언한다.
sensor = Adafruit_DHT.DHT11

# DHT11 센서와 연결된 핀을 정의한다.
pin = 27

if __name__ == "__main__":
 
    # 무한 반복하여센서의정보를1초에한번씩출력한다.
    while(True):
        # 습도 데이터를센서로부터가져온다.
        sensorValue = Adafruit_DHT.read(sensor, pin)
        temperature = sensorValue[1]
        # 만약 습도데이터가None 값이아니라면값을출력한다.
        if temperature is not None:
            print('Temperatrue={}°C'.format(temperature))
        else:
            print('Failed to get reading. Try again!')

        # 2초간 대기한다.
        time.sleep(2.0)