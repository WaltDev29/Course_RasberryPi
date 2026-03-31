'''
2026.03.31
온습도 센서 읽기
'''
import Adafruit_DHT
import time

# DHT11 센서 객체를 선언.
sensor = Adafruit_DHT.DHT11

# DHT11 센서와 연결된 핀을 정의.
PIN = 27


# 센서의 정보를 1초에 한번씩 출력.
if __name__ == "__main__":
    while (True):

        # 습도 데이터를 센서로부터 가져온다.
        humidity,temperature = Adafruit_DHT.read_retry(sensor, PIN) # read가 아닌 read_retry함수 : read가 성공할 때까지 일정횟수(기본값 : 15) 일정 시간(기본값 : 2초)마다 시도
        
        print(f"Humidity : {humidity}%  Temperature : {temperature}°C", end="\n\n")