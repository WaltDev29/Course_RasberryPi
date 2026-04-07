import smbus
import time


# LED 제어 비트
RED_LED = 0b00000001
GREEN_LED = 0b00000010
BLUE_LED = 0b00000100
state = None
bus = None


# i2c를 사용하기 위해 smbus 모듈 초기화
def ledInit():
    global state
    global bus
    state = 0b00000000
    bus = smbus.SMBus(1)

def ledOn(cmd):
    global state
    state = (state | cmd)
    bus.write_byte(0x20, state)

def ledOff(cmd):
    global state
    state = (state & (~cmd))
    bus.write_byte(0x20, state)



ledInit()
ledOn(RED_LED)
time.sleep(0.5)

ledOn(GREEN_LED)
time.sleep(0.5)

ledOn(BLUE_LED)
time.sleep(0.5)

ledOff(RED_LED)
time.sleep(0.5)

ledOff(GREEN_LED)
time.sleep(0.5)

ledOff(BLUE_LED)
time.sleep(0.5)

ledOn(RED_LED)
ledOn(GREEN_LED)
ledOn(BLUE_LED)
time.sleep(1)

ledOff(RED_LED)
ledOff(GREEN_LED)
ledOff(BLUE_LED)
time.sleep(1)