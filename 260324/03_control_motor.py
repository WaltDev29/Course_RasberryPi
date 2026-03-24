import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# ============ PIN 설정 ============
MOTOR_P=19
MOTOR_N=13

SW1_PIN = 4
SW2_PIN = 17
SW3_PIN = 18
SW_PIN_LIST = [SW1_PIN, SW2_PIN, SW3_PIN]

GPIO.setup(MOTOR_P, GPIO.OUT)
GPIO.setup(MOTOR_N, GPIO.OUT)
GPIO.setup(SW_PIN_LIST, GPIO.IN)



# ============ Main Loop 실행 ============
if __name__ == "__main__":
    try:
        while True:
            # ============ 버튼 상태 읽기 ============
            button_state = []
            for btn in SW_PIN_LIST:
                button_state.append(GPIO.input(btn))

            # ============ 모터 정지 ============
            GPIO.output(MOTOR_P, GPIO.LOW)
            GPIO.output(MOTOR_N, GPIO.LOW)

            # ============ 버튼 상태에 따라 모터 조작 ============
            if not button_state[0]:
                GPIO.output(MOTOR_P, GPIO.HIGH)

            elif not button_state[1]:
                GPIO.output(MOTOR_N, GPIO.HIGH)
            
            elif not button_state[2]:
                break

        time.sleep(0.01) # CPU 보호

    finally:
        GPIO.cleanup() # 메모리 정리