# I2C 사용을 위한 모듈
import smbus
# 지연시간 제어를 위한 모듈
import time

# I2C 버스 객체 생성
bus = smbus.SMBus(1)

# I2C 주소 (PCF8591)
i2c_address = 0x48

# PCF8591에서 데이터를 읽기 위한 명령어
command = 0x44

try:
    while True:
        # i2c의 주소와 명령어를 전송하여 5Byte 데이터를 읽어온다.
        # index 0은 dummy data, 실제 ADC 값은 index 1~4
        adc_data = bus.read_i2c_block_data(i2c_address, command, 5)

        # ADC0 (가변저항) 값 읽기
        VrValue = adc_data[1]

        # 퍼센트 변환 (0~255 → 0~100)
        VrValue = VrValue * 100 / 255
        VrValue = round(VrValue, 2)

        print("가변저항 : " + str(VrValue) + " %")

        time.sleep(0.1)

# Ctrl + C 입력 시 종료
except KeyboardInterrupt:
    pass