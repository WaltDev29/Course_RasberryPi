from tkinter import *
import RPi.GPIO as GPIO
import time
import threading

trig = 23
echo = 24

class MainFrame(Frame):
    def __init__(self, master):
        super().__init__(master)
        master.title('Ultrasonic Control Example')
        master.geometry("400x300+10+10")

        # 상단 제목 및 학번 표시
        self.titleLabel = Label(master, text="Distance Alert  |  2401110265", font=("Arial", 12, "bold"))
        self.titleLabel.pack(pady=10, anchor='ne', padx=10)

        # 사각형 모양 Label (크기와 색상으로 표현)
        self.boxLabel = Label(master, width=20, height=10, bg="gray", relief="ridge", bd=2)
        self.boxLabel.pack(pady=10)

        # 거리값 표시 Label
        self.distanceLabel = Label(master, text="Distance: -- cm", font=("Arial", 12))
        self.distanceLabel.pack()

        # 거리 측정 쓰레드
        self.t = threading.Thread(target=self.UltrasonicMonitor)
        self.t.daemon = True
        self.t.start()

    def UltrasonicMonitor(self):
        try:
            while True:
                GPIO.output(trig, GPIO.LOW)
                time.sleep(0.05)
                GPIO.output(trig, GPIO.HIGH)
                time.sleep(0.00001)
                GPIO.output(trig, GPIO.LOW)

                while GPIO.input(echo) == 0:
                    signal_Start = time.time()
                while GPIO.input(echo) == 1:
                    signal_End = time.time()

                duration = signal_End - signal_Start
                distance = round((duration * 34000) / 2, 2)

                if distance < 1000:
                    self.updateUI(distance)
                time.sleep(0.2)
        except Exception as e:
            print("Error:", e)
            time.sleep(1)

    def updateUI(self, distance):
        # 거리값 텍스트 업데이트
        self.distanceLabel.config(text=f"Distance: {distance} cm")

        # 배경색 결정
        if distance < 20:
            color = "red"
        elif distance < 50:
            color = "green"
        else:
            color = "blue"

        # 사각형(Label) 색상 변경
        self.boxLabel.config(bg=color)

# GPIO 초기화
def GPIO_Ultrasonic_init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(trig, GPIO.OUT)
    GPIO.setup(echo, GPIO.IN)

if __name__ == "__main__":
    GPIO_Ultrasonic_init()
    root = Tk()
    app = MainFrame(root)
    root.mainloop()
    GPIO.cleanup()
