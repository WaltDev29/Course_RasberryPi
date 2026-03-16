import RPi.GPIO as GPIO
import time
 
# 스텝모터와 연결된GPIO 번호를변수에저장한다.
STEP_IN1 = 16
STEP_IN2 = 20
STEP_IN3 = 21
STEP_IN4 = 26

pinsArray = [STEP_IN1,STEP_IN2,STEP_IN3,STEP_IN4] 

# 풀 스탭 구동(1상 여자방식)
signal_full = [
        [GPIO.HIGH, GPIO.LOW, GPIO.LOW, GPIO.LOW],
        [GPIO.LOW, GPIO.HIGH, GPIO.LOW, GPIO.LOW],
        [GPIO.LOW, GPIO.LOW, GPIO.HIGH, GPIO.LOW],
        [GPIO.LOW, GPIO.LOW, GPIO.LOW, GPIO.HIGH]
        ]

# 1스탭의 사이클
FULL_STEP = len(pinsArray)
ROTATE_360_STEP = 512 # FULL_STEP으로 512스탭

if __name__ == "__main__":

    # BCM 핀맵을사용한다
    GPIO.setmode(GPIO.BCM)
    for p_index in pinsArray:
        GPIO.setup(p_index, GPIO.OUT)
        GPIO.output(p_index, GPIO.LOW)

# 반복하여 모터를정방향-> 정지-> 역방향-> 정지 순서로 제어한다.
    try:
        for i in range(0,ROTATE_360_STEP):
            for step_idx in range(FULL_STEP):
                for idx in range(4):
                    GPIO.output(pinsArray[idx], signal_full[step_idx][idx])
                time.sleep(0.002)
        
        for i in range(0,ROTATE_360_STEP):
            for step_idx in reversed(range(FULL_STEP)):
                for idx in range(4):
                    GPIO.output(pinsArray[idx], signal_full[step_idx][idx])
                time.sleep(0.002)

# 키보드 인터럽트, 에러 등으로 소스가 종료될 경우 GPIO를 초기화 한 후 종료한다.
    finally:
        GPIO.cleanup()
    
