import RPi.GPIO as GPIO
import time

# GPIO의 모드를 BCM으로 설정한다(GPIO번호 사용)
GPIO.setmode(GPIO.BCM)
SW1_PIN = 4
SW2_PIN = 17
SW3_PIN = 18
SW4_PIN = 22
SW_PIN_LIST = [SW1_PIN, SW2_PIN, SW3_PIN, SW4_PIN]

if __name__ == "__main__":
 # GPIO 핀을 INPUT 으로 설정한다.
    GPIO.setup(SW_PIN_LIST, GPIO.IN)
    try:
        while(True):
            button_state = []
            for i in SW_PIN_LIST:
                button_state.append(GPIO.input(i))  # 버튼이 눌리면 LOW/0, 눌리지 않으면 HIGH/1 반환

            print("Button State : ", button_state)
            
            # 0.5초간 대기한다.
            time.sleep(0.5)
    finally:
        GPIO.cleanup()