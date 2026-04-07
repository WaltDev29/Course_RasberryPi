import RPi.GPIO as GPIO
import time

# GPIO 모드를 BCM으로 설정 (GPIO 번호 사용)
GPIO.setmode(GPIO.BCM)

# 서보모터 핀 번호
SERVO_PIN = 25

if __name__ == "__main__":
    # 서보모터 핀을 OUTPUT으로 설정
    GPIO.setup(SERVO_PIN, GPIO.OUT)

    # PWM 생성 (50Hz → 서보모터 표준 주파수)
    servo_pwm = GPIO.PWM(SERVO_PIN, 50)

    # PWM 시작 (초기 duty 0)
    servo_pwm.start(0)

    try:
        while True:
            # 0도 (중앙)
            servo_pwm.ChangeDutyCycle(7.5)
            time.sleep(1)

            # -90도 (왼쪽)
            servo_pwm.ChangeDutyCycle(2.5)
            time.sleep(1)

            # 다시 0도
            servo_pwm.ChangeDutyCycle(7.5)
            time.sleep(1)

            # 90도 (오른쪽)
            servo_pwm.ChangeDutyCycle(12.5)
            time.sleep(1)

    except KeyboardInterrupt:
        print("프로그램 종료")

    finally:
        servo_pwm.stop()   # PWM 종료
        GPIO.cleanup()     # GPIO 초기화