import RPi_I2C_driver


textLcd = RPi_I2C_driver.lcd()

textLcd.lcd_display_string("Hello", 1)
textLcd.lcd_display_string("World", 2)