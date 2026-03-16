'''
2026.03.16
# 자기장 이동 방식의 Step Motor 제어
'''
import RPi.GPIO as GPIO
import time
 
# ============ 스텝모터 핀 연결 ============
STEP_IN1 = 16
STEP_IN2 = 20
STEP_IN3 = 21
STEP_IN4 = 26

pinsArray = [STEP_IN1,STEP_IN2,STEP_IN3,STEP_IN4] 


# ============ 풀 스탭 구동(1상 여자방식) ============
'''
스텝 모터의 코일을 순서대로 켜서 자기장 이동으로 모터를 회전 시킴.
'''
signal_full = [
        [GPIO.HIGH, GPIO.LOW, GPIO.LOW, GPIO.LOW],
        [GPIO.LOW, GPIO.HIGH, GPIO.LOW, GPIO.LOW],
        [GPIO.LOW, GPIO.LOW, GPIO.HIGH, GPIO.LOW],
        [GPIO.LOW, GPIO.LOW, GPIO.LOW, GPIO.HIGH]
        ]


# ============ 1스탭의 사이클 ============
FULL_STEP = len(pinsArray)
ROTATE_360_STEP = 512 # FULL_STEP으로 512스탭



if __name__ == "__main__":
    # ============ 핀 맵 설정 ============
    GPIO.setmode(GPIO.BCM)
    for p_index in pinsArray:
        GPIO.setup(p_index, GPIO.OUT)
        GPIO.output(p_index, GPIO.LOW)


    try:
        # ============ 정방향 회전 ============ 
        for i in range(0,ROTATE_360_STEP): # 512번 루프
            for step_idx in range(FULL_STEP): # 4번 루프 (1,2,3,4 코일 차례로 켜기)
                for idx in range(4): # 각 모터에 값 전송 (ex. [P,N,N,N])
                    GPIO.output(pinsArray[idx], signal_full[step_idx][idx])
                time.sleep(0.002)
        
        # ============ 역방향 회전 ============ 
        for i in range(0,ROTATE_360_STEP):
            for step_idx in reversed(range(FULL_STEP)):
                for idx in range(4):
                    GPIO.output(pinsArray[idx], signal_full[step_idx][idx])
                time.sleep(0.002)


    finally:
        GPIO.cleanup()
    
