import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

buzzer = 12

# 4옥타브 도레미~ 5옥타브 도
SCALE = [261, 294, 330, 349, 392, 440, 493, 523]

GPIO.setup(buzzer, GPIO.OUT)
pwm = GPIO.PWM(buzzer, 100) # 100Hz

try:
    # pwm 시작
    pwm.start(100)
    # dutycycle 50%
    pwm.ChangeDutyCycle(50)

    for i in SCALE:
        pwm.ChangeFrequency(i) #주파수 변경
        time.sleep(0.5)

    # Buzzer를 끈다
    pwm.ChangeDutyCycle(100)
    print("OFF")

# 종료 등의 키보드 인터럽트 발생시 처리 동작
except KeyboardInterrupt:
    print("프로그램 종료")

finally:
    # Buzzer를 끈다
    pwm.stop()
    GPIO.output(buzzer,GPIO.LOW)

    # GPIO를 초기화한다
    GPIO.cleanup()