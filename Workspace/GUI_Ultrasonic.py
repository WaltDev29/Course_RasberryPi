    from tkinter import *
import RPi.GPIO as GPIO
import time
import threading
trig = 23
echo = 24

# 프로그램의 창을생성하는MainFrame 클래스
class MainFrame(Frame):

    # MainFrame 클래스의 생성자.
    # self는 객체의 인스턴스를 의미하며, master는 부모 객체를 의미한다. 여기서는 Tk를 의미한다.
    def __init__(self, master):
        master.title('Ultasonic Control Example')

        # 윈도우 크기및좌표를속성으로한다.
        master.geometry("400x240+10+10")

        # 초음파센서의 textvariable 옵션에 사용될 상태를 저장하는 변수 리스트
        self.buttonState = StringVar()

        # 선언된 배열의크기만큼반복하며메세지를초기화한다.
        # Label은 textvariable 옵션을 통해 넘긴 변수로 데이터를 변경한다
        # for i in range(0,len(self.buttonState)):
        self.buttonState.set("Ultrasonic : " + str(0))

        # 초음파센서의 상태를표시할라벨위젯의객체리스트를정의한다
        self.usnLabel = Label(master,background="yellow", textvariable = self.buttonState)
        self.usnLabel.pack(side = LEFT, expand = 1)

        # 실시간으로 상태를변경시키는UltasonicStateThread 동작 시키기 위한 스레드 생성
        self.t = threading.Thread(target=self.UltasonicStateThread)
        self.t.start()

    # 초음파센서를 이용해거리를측정하는스레드
    def UltasonicStateThread(self) :
        try :
            while(True):
                # 거리 측정을위해초음파를쏜다
                GPIO.output(trig, GPIO.LOW)
                time.sleep(0.5)
                GPIO.output(trig, GPIO.HIGH)
                time.sleep(0.00001)
                GPIO.output(trig, GPIO.LOW)
                while (GPIO.input(echo) == 0) :
                    signal_Start = time.time()
                while (GPIO.input(echo) == 1) :
                    signal_End = time.time()

                # 응답 받은시간과초음파의속도등으로거리를계산한다
                responseDuration = signal_End- signal_Start
                distance = responseDuration * 34000 / 2 # (34000cm/s) 왕복이므로 2를 나누어준다

                # 소수점 둘째자리까지만출력한다
                distance = round(distance, 2)
                
                # 1000cm 를 초과할시 값을표기하지않는다
                if distance < 1000 : 
                    self.buttonState.set("Distance : " + str(distance) + "cm")
                else:
                    pass
                time.sleep(0.1)
        except Exception as err: 
            time.sleep(1)
            print(err)
 
# GPIO를 사용하기전 초기화하는함수
def GPIO_Ultasonic_init():
    # BCM 핀맵을사용한다
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(trig, GPIO.OUT)
    GPIO.setup(echo, GPIO.IN)

# 프로그램의 메인에해당하는최상위구문
if (__name__ == '__main__'):
    GPIO_Ultasonic_init()
    root = Tk()                # 창을 띄우기 위한 객체를선언
    mainFrame = MainFrame(root) # 창 객체를 인자로 클래스를 생성한다
    root.mainloop()             # python의 창을 띄우고 이벤트처리수행함수
    GPIO.cleanup()              # 창종료후GPIO를초기화한다.
    sys.exit()                 # 소프트웨어를 완전히 종료한다.