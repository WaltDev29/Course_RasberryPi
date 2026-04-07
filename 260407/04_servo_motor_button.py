import RPi.GPIO as GPIO
import time

# GPIO 모드를 BCM으로 설정 (GPIO 번호 사용)
GPIO.setmode(GPIO.BCM)

# 서보모터 핀 번호
SERVO_PIN = 25
SW1_PIN = 4
SW2_PIN = 17
SW_PIN_LIST = [SW1_PIN, SW2_PIN]

num = 7.5  # 초기값 (0도 위치)

if __name__ == "__main__":
    # 서보모터 핀을 OUTPUT으로 설정
    GPIO.setup(SERVO_PIN, GPIO.OUT)
    GPIO.setup(SW_PIN_LIST, GPIO.IN)

    # PWM 생성 (50Hz → 서보모터 표준 주파수)
    servo_pwm = GPIO.PWM(SERVO_PIN, 50)

    # PWM 시작 (초기 duty 0)
    servo_pwm.start(0)

    try:
        while(True):
            button_state = []
            for i in SW_PIN_LIST:
                button_state.append(GPIO.input(i))  # 버튼이 눌리면 LOW/0, 눌리지 않으면 HIGH/1 반환

            if button_state[0] == 0:  # SW1이 눌렸을 때
                num -= 0.2
                if num <= 2.5:  # 최소값 제한
                    num = 2.5
                servo_pwm.ChangeDutyCycle(num) # 왼쪽
            elif button_state[1] == 0:  # SW2가 눌렸을 때
                num += 0.2
                if num >= 12.5:  # 최대값 제한
                    num = 12.5
                servo_pwm.ChangeDutyCycle(num)  # 오른쪽

            print("Button State : ", button_state)
            
            # 0.5초간 대기한다.
            time.sleep(0.1)

    except KeyboardInterrupt:
        print("프로그램 종료")

    finally:
        servo_pwm.stop()   # PWM 종료
        GPIO.cleanup()     # GPIO 초기화