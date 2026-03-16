import smbus
import time
import math
 
class read_i2c:
 
    # i2c 사용하기 위해서 하는 기본 설정
    def __init__(self, i2c_address=0x48):
        self.bus = smbus.SMBus(1)
        self.i2c_address = i2c_address
        self.command = 0x44
        #sm 버스 등록
 
    #가변저항 값 읽어오기
    # 0x44 명령어로 5Byte 읽어온다
    def vr_read(self):
        adc_data = bus.read_i2c_block_data(self.i2c_address, self.command, 5)
        # I2C로 부터 센서 값을 읽어온다 VR 센서는 ADC 0번이다.
        VrValue = adc_data[1]
        VrValue = VrValue * 100 / 251
        VrValue = round(VrValue, 2)
        return VrValue
 
    #psd 센서 값 읽어오기
    def psd_read(self):     
        adc_data = self.bus.read_i2c_block_data(self.i2c_address, self.command, 5)
        psd_value = (adc_data[4] / 255.0 * 3.3) * 3 / 2
        psd_value = 29.988 * math.pow(psd_value, -1.173)
        return round(psd_value, 2)
    #가스 센서 값 읽어오기
    def gas_read(self):
        adc_data = self.bus.read_i2c_block_data(self.i2c_address, self.command, 5)
        VrValue = adc_data[3]
        return VrValue
    #CdS 센서 값 읽어오기
    def cds_read(self):
        adc_data = self.bus.read_i2c_block_data(self.i2c_address, self.command, 5)
        VrValue = adc_data[2]
        VrValue = VrValue * 100 / 251
        VrValue = round(VrValue, 2)
        return VrValue
class write_i2c:
    state = 0b00000001
    global bus
    bus = smbus.SMBus(1)
 
    def On(self, cmd):  # self 추가
        self.state = (self.state | cmd)
        bus.write_byte(0x20, self.state)
 
    def Off(self, cmd):  # self 추가
        self.state = (self.state & (~cmd))
        bus.write_byte(0x20, self.state)