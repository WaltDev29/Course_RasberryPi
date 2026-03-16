import smbus
import math

class read_i2c:
    bus = None
    i2c_address = 0x48  
    command = 0x44

    def __init__(self):
        self.bus = smbus.SMBus(1)
        
    def vr_read(self):
        # ADC 데이터 읽기
        adc_data = self.bus.read_i2c_block_data(self.i2c_address, self.command, 5)
        # 첫 바이트는 더미 데이터이므로 무시하고 두 번째 바이트가 VR 데이터
        VrValue = adc_data[1] * 100 / 255
        return round(VrValue, 2)

    def cds_read(self):
        # CDS 센서 데이터 (3번째 바이트)
        adc_data = self.bus.read_i2c_block_data(self.i2c_address, self.command, 5)
        CdsValue = adc_data[2] * 100 / 255
        return round(CdsValue, 2)

    def gas_read(self):
        # 가스 센서 데이터 (4번째 바이트)
        adc_data = self.bus.read_i2c_block_data(self.i2c_address, self.command, 5)
        GasValue = adc_data[3]
        return GasValue

    def psd_read(self):
        # PSD 센서 데이터 (5번째 바이트)
        adc_data = self.bus.read_i2c_block_data(self.i2c_address, self.command, 5)
        psd_value = (adc_data[4] / 255.0 * 3.3) * 3 / 2
        psd_value = 29.988 * math.pow(psd_value, -1.173)
        return round(psd_value, 2)

class write_i2c:
    state = 0b00000000
    bus = None
    i2c_address = 0x20  # 4주차 자료에 따르면 기본 주소는 0x20

    def __init__(self):
        self.bus = smbus.SMBus(1)

    def On(self, cmd):
        # LED 켜기
        self.state = self.state | cmd
        self.bus.write_byte(self.i2c_address, self.state)

    def Off(self, cmd):
        # LED 끄기
        self.state = self.state & (~cmd)
        self.bus.write_byte(self.i2c_address, self.state)