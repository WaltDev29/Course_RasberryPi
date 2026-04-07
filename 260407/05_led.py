import smbus
import time


RED_LED = 0b00000001
GREEN_LED = 0b00000010
BLUE_LED = 0b00000100


bus = smbus.SMBus(1)


# ============ ON ============
# RED LED ON
bus.write_byte(0x20, RED_LED)
time.sleep(0.5)

# GREEN LED ON
bus.write_byte(0x20, GREEN_LED)
time.sleep(0.5)

# BLUE LED ON
bus.write_byte(0x20, BLUE_LED)
time.sleep(0.5)
state = RED_LED | GREEN_LED | BLUE_LED

# All LED ON
bus.write_byte(0x20, state)
time.sleep(0.5)



# ============ OFF ============
# Blue OFF
state = state & (~BLUE_LED)
# GREEN And RED LED ON
bus.write_byte(0x20, state)
time.sleep(0.5)

# Green OFF
state = state & (~GREEN_LED)
# RED LED ON
bus.write_byte(0x20, state)
time.sleep(0.5)

# Red OFF
state = state & (~RED_LED)
bus.write_byte(0x20, state)
time.sleep(0.5)

state = RED_LED | GREEN_LED | BLUE_LED
bus.write_byte(0x20, state)