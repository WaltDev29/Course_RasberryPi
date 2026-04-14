# I2C 사용을 위한 모듈
import smbus
# 지연시간 제어를 위한 모듈
import time

bus = smbus.SMBus(1)
i2c_address = 0x48

# PCF8591 칩에서 데이터를 받기 위한 명령어
command = 0x44

# Ctrl + C로 종료 가능
try:
    while True:
        # 5바이트 읽기 (0번은 dummy, 1~4가 실제 ADC 값)
        adc_data = bus.read_i2c_block_data(i2c_address, command, 5)

        # GAS 센서 값 (ADC2 → index 3)
        GAS = adc_data[3]

        print("GAS : " + str(GAS))

        time.sleep(0.1)

# 키보드 인터럽트 처리
except KeyboardInterrupt:
    pass