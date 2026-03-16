from tkinter import *
import Adafruit_DHT
import time
import threading
sensor = Adafruit_DHT.DHT11
pin = 27

# 프로그램의 창을생성하는MainFrame 클래스
class MainFrame(Frame):
 # MainFrame 클래스의 생성자.
 # self는 객체의 인스턴스를 의미하며, master는 부모 객체를 의미한다. 여기서는 Tk를 의미한다.
 def __init__(self, master):
 master.title('Temperature,Humidity Example')
 # 윈도우 크기및좌표를속성으로한다.
 master.geometry("400x240+10+10")
 # 온습도센서의 textvariable 옵션에 사용될 상태를 저장하는 변수 리스트
self.value = StringVar()
 # Label은 textvariable 옵션을 통해 넘긴 변수(value)로 데이터를 변경한다
self.value.set('Temp={}°C  Humidity={}%'.format('-', '-'))
 # 온습도센서의 상태를표시할Label 위젯의 객체정의한다
self.tempLabel = Label(master,background="yellow", textvariable = self.value)
 self.tempLabel.pack(side = LEFT, expand = 1)
 # 실시간으로 상태를변경시키는analogReadThread 동작 시키기 위한 스레드 생성
self.t = threading.Thread(target=self.analogReadThread)
 self.t.start()