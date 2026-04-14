import smbus
import time

# Relay 제어 비트
RELAY_1 = 0b00010000
RELAY_2 = 0b00100000

state = None
bus = None

##########################
# RELAY 제어 함수
##########################

# i2c를 사용하기 위해 smbus 모듈을 초기화한다.
def relayInit():
    global state
    global bus
    state = 0b00000000
    bus = smbus.SMBus(1)


def relayOn(cmd):
    global state
    # RELAY는 bit로 제어되기 때문에 논리 연산자를 사용한다.
    # | 는 OR를 의미한다.
    state = state | cmd
    bus.write_byte(0x20, state)


def relayOff(cmd):
    global state
    # RELAY는 bit로 제어되기 때문에 논리 연산자를 사용한다.
    # not cmd를 만들고 state와 AND하여 원하는 비트만 OFF시킨다.
    state = state & (~cmd)
    bus.write_byte(0x20, state)


# 초기화
relayInit()

# 릴레이1 ON/OFF
relayOn(RELAY_1)
time.sleep(0.5)
relayOff(RELAY_1)
time.sleep(0.5)

# 릴레이2 ON/OFF
relayOn(RELAY_2)
time.sleep(0.5)
relayOff(RELAY_2)
time.sleep(0.5)

# 릴레이1, 2 ON
relayOn(RELAY_1)
relayOn(RELAY_2)
time.sleep(1)

# 릴레이1, 2 OFF
relayOff(RELAY_1)
relayOff(RELAY_2)
time.sleep(1)