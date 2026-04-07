import RPi.GPIO as GPIO
import time

# 핀 설정 (BCM 12번 핀 사용)
BUZZER_PIN = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

# PWM 객체 생성 (초기 주파수 440Hz)
pwm = GPIO.PWM(BUZZER_PIN, 440)

# 음계별 주파수 정의 (Hz)
notes = {
    'D4': 294, 'D5': 587, 'A4': 440, 'GS4': 415, 
    'G4': 392, 'F4': 349, 'C4': 262, 'B3': 247, 
    'AS3': 233, 'OFF': 0
}

# 메갈로바니아 멜로디 구성 (음표, 지속시간)
# 지속시간 단위: 0.125는 8분음표 정도의 속도
melody = [
    ('D4', 0.1), ('D4', 0.1), ('D5', 0.2), ('A4', 0.2), 
    ('OFF', 0.1), ('GS4', 0.2), ('OFF', 0.1), ('G4', 0.2), 
    ('OFF', 0.1), ('F4', 0.2), ('D4', 0.1), ('F4', 0.1), ('G4', 0.1)
]

def play_tone(frequency, duration):
    if frequency == 0:
        pwm.ChangeDutyCycle(0) # 소리 끄기
    else:
        pwm.ChangeDutyCycle(50) # Duty Cycle 50%로 소리 발생
        pwm.ChangeFrequency(frequency)
    
    time.sleep(duration)
    pwm.ChangeDutyCycle(0) # 음 사이 간격

try:
    print("Megalovania 연주를 시작합니다... (Ctrl+C로 중단)")
    pwm.start(0)

    # 4번 반복 (메갈로바니아 루프 특징)
    for _ in range(4):
        for note, duration in melody:
            play_tone(notes[note], duration)
            time.sleep(duration * 0.1) # 음 분리를 위한 미세한 휴식

finally:
    pwm.stop()
    GPIO.cleanup()
    print("프로그램 종료")