'''
2026.03.16
# RPi.GPIO 실습
    - DC 모터 조작
    - 
'''

import RPi.GPIO as GPIO
import time


# ============ 모드 설정 ============
GPIO.setmode(GPIO.BCM) # BCM 핀 맵 사용
GPIO.setwarnings(False)

MOTOR_P=19
MOTOR_M=13

GPIO.setup(MOTOR_M, GPIO.OUT) # 13번 핀(DC모터)를 OUTPUT 상태로 설정
GPIO.setup(MOTOR_P, GPIO.OUT) # 19번 핀(DC모터)를 OUTPUT 상태로 설정


if __name__ == "__main__":
    try:
        for i in range(3):
            # ============ 모터 제어 ============
            '''
            - 서로 다른 값을 주어야 돌아감
            - 한 번 값을 주면 계속 유지됨.
            '''
            GPIO.output(MOTOR_M, GPIO.HIGH)  # HIGH/1/True
            GPIO.output(MOTOR_P, GPIO.LOW)   # LOW/0/False
            time.sleep(1)

            GPIO.output(MOTOR_M, GPIO.LOW)
            GPIO.output(MOTOR_P, GPIO.HIGH)
            time.sleep(1)

    except Exception as e:
        print(f"에러 타입 : {type(e).__name__}")
        print(f"에러 메시지 : {e}")

    finally:
        # ============ 모터 정지 ============
        '''둘 다 LOW로 줘야 정지함.'''
        GPIO.output(MOTOR_M, GPIO.LOW)
        GPIO.output(MOTOR_P, GPIO.LOW)

        # GPIO 핀 상태 초기화
        GPIO.cleanup()