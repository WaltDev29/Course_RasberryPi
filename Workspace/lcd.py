import I2C_LCD_driver

fontdata1 = [
        # Char 0 - Upper-left
        [ 0x00, 0x00, 0x03, 0x04, 0x08, 0x19, 0x11, 0x10 ],
        # Char 1 - Upper-middle
        [ 0x00, 0x1F, 0x00, 0x00, 0x00, 0x11, 0x11, 0x00 ],
        # Char 2 - Upper-right
        [ 0x00, 0x00, 0x18, 0x04, 0x02, 0x13, 0x11, 0x01 ],
        # Char 3 - Lower-left
        [ 0x12, 0x13, 0x1b, 0x09, 0x04, 0x03, 0x00, 0x00 ],
        # Char 4 - Lower-middle
        [ 0x00, 0x11, 0x1f, 0x1f, 0x0e, 0x00, 0x1F, 0x00 ],
        # Char 5 - Lower-right
        [ 0x09, 0x19, 0x1b, 0x12, 0x04, 0x18, 0x00, 0x00 ],
        # Char 6 - my test
	[ 0x1f,0x0,0x4,0xe,0x0,0x1f,0x1f,0x1f],
]


# I2C_LCD_Driver 모듈을 사용하는 예제
textLcd = I2C_LCD_driver.lcd()

# 16자 이내 아스키코드, 1은 첫 번째 줄이고 2는 두 번째 줄이다
#textLcd.lcd_display_string("ABCDEFG", 1, 2)
#textLcd.lcd_display_string("123456", 2)
textLcd.lcd_load_custom_chars(fontdata1)


# Write first three chars to row 1 directly
textLcd.lcd_write(0x80)
textLcd.lcd_write_char(0)
textLcd.lcd_write_char(1)
textLcd.lcd_write_char(2)
# Write next three chars to row 2 directly
textLcd.lcd_write(0xC0)
textLcd.lcd_write_char(3)
textLcd.lcd_write_char(4)
textLcd.lcd_write_char(5)
sleep(2)

