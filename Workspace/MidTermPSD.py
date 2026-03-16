from i2c_class import read_i2c, write_i2c
import I2C_LCD_driver
import time

# 학번 설정
STUDENT_ID = "ID: 2401110265"

# LED 제어 비트
RED_LED = 0b00000001
GREEN_LED = 0b00000010
BLUE_LED = 0b00000100

# I2C 장치 초기화
adc = read_i2c()
write = write_i2c()
lcd = I2C_LCD_driver.lcd()

# LCD 초기 메시지 출력
lcd.lcd_display_string(STUDENT_ID, 1)

def update_display_and_led(distance_cm):
    # 거리값 출력 (2열)
    lcd.lcd_display_string(f"range: {distance_cm} cm", 2)
    
    # LED 제어 로직
    if 20 <= distance_cm <= 30:
        write.On(RED_LED)
        write.Off(GREEN_LED | BLUE_LED)
    elif 31 <= distance_cm <= 50:
        write.On(GREEN_LED)
        write.Off(RED_LED | BLUE_LED)
    elif 51 <= distance_cm <= 100:
        write.On(BLUE_LED)
        write.Off(RED_LED | GREEN_LED)
    else:
        write.On(RED_LED | GREEN_LED | BLUE_LED)

try:
    while True:
        # PSD 센서로부터 거리값 읽기
        distance = adc.psd_read()
        # LCD 및 LED 상태 업데이트
        update_display_and_led(distance)
        # 주기적으로 갱신 (0.5초)
        time.sleep(0.5)
except KeyboardInterrupt:
    # 종료시 모든 LED 끄기
    write.Off(RED_LED | GREEN_LED | BLUE_LED)
    lcd.lcd_clear()
    print("프로그램 종료")