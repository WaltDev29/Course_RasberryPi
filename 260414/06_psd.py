# I2C 사용을 위한 모듈
import smbus
# 지연시간 제어를 위한 모듈
import time
import math

bus = smbus.SMBus(1)
i2c_address = 0x48

# PCF8591 칩에서 데이터를 받기 위한 명령어
command = 0x44

# Ctrl + C로 종료 가능
try:
    while True:
        # 5바이트 읽기 (0번은 dummy, 1~4가 실제 ADC 값)
        adc_data = bus.read_i2c_block_data(i2c_address, command, 5)

        # PSD 센서 값 (ADC3 → index 4)
        # 전압 계산 → (ADC값 / 255 * 3.3V)
        # 전압 분배 보정 → * 3 / 2
        psd_voltage = (adc_data[4] / 255.0 * 3.3) * 3 / 2

        # 거리 계산 공식
        psd_value = 29.988 * math.pow(psd_voltage, -1.173)

        psd_value = round(psd_value, 2)

        print("PSD : " + str(psd_value) + " cm")

        time.sleep(0.1)

# 키보드 인터럽트 처리
except KeyboardInterrupt:
    pass