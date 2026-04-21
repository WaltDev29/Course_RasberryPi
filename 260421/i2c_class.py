# i2c_class.py 파일
import smbus
import math


class read_i2c:
    bus = None
    i2c_address = None
    command = 0x44

    def __init__(self):
        self.bus = smbus.SMBus(1)
        self.i2c_address = 0x48

    def read_data(self):
        return self.bus.read_i2c_block_data(self.i2c_address, self.command, 5)

    def vr_read(self):
        data = self.read_data()[1]
        return data * 100 / 255

    def cds_read(self):
        data = self.read_data()[2]
        return data * 100 / 255

    def gas_read(self):
        data = self.read_data()[3]
        return data

    def psd_read(self):
        data = self.read_data()[4]

        psd_voltage = (data / 255.0 * 3.3) * 3 / 2

        psd_value = 29.988 * math.pow(psd_voltage, -1.173)

        psd_value = round(psd_value, 2)
        return psd_value


class write_i2c:
    addr = 0x20

    def __init__(self):
        self.bus = smbus.SMBus(1)
        self.state = 0b00000000

    def on(self, value):
        self.state |= value
        self.bus.write_byte(self.addr, self.state)

    def off(self, value):
        self.state &= ~value
        self.bus.write_byte(self.addr, self.state)