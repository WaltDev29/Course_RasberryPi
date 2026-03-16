from tkinter import *
import smbus

RED_LED   = 0b00000001
GREEN_LED = 0b00000010
BLUE_LED  = 0b00000100

class MainFrame(Frame):

    def __init__(self, master):
        master.title('LED Control Example')
        master.geometry("400x240+10+10")

        redLedOnButton = Button(master, background="RED", text="RED LED ON",
                                command=lambda: self.onButtonClickEvent(0))
        redLedOnButton.pack(expand=1)

        redLedOffButton = Button(master, background="RED", text="RED LED OFF",
                                 command=lambda: self.onButtonClickEvent(1))
        redLedOffButton.pack(expand=1)

        greenLedOnButton = Button(master, background="GREEN", text="GREEN LED ON",
                                  command=lambda: self.onButtonClickEvent(2))
        greenLedOnButton.pack(expand=1)

        greenLedOffButton = Button(master, background="GREEN", text="GREEN LED OFF",
                                   command=lambda: self.onButtonClickEvent(3))
        greenLedOffButton.pack(expand=1)

        blueLedOnButton = Button(master, background="BLUE", text="BLUE LED ON",
                                 command=lambda: self.onButtonClickEvent(4))
        blueLedOnButton.pack(expand=1)

        blueLedOffButton = Button(master, background="BLUE", text="BLUE LED OFF",
                                  command=lambda: self.onButtonClickEvent(5))
        blueLedOffButton.pack(expand=1)

        self.ledInit()

    def onButtonClickEvent(self, pin):
        if pin == 0:
            self.ledOn(RED_LED)
        elif pin == 1:
            self.ledOff(RED_LED)
        elif pin == 2:
            self.ledOn(GREEN_LED)
        elif pin == 3:
            self.ledOff(GREEN_LED)
        elif pin == 4:
            self.ledOn(BLUE_LED)
        elif pin == 5:
            self.ledOff(BLUE_LED)

    def ledInit(self):
        self.state = 0b00000000
        self.bus = smbus.SMBus(1)

    def ledOn(self, cmd):
        self.state = (self.state | cmd)
        self.bus.write_byte(0x20, self.state)

    def ledOff(self, cmd):
        self.state = (self.state & (~cmd))
        self.bus.write_byte(0x20, self.state)

if __name__ == '__main__':
    root = Tk()
    mainFrame = MainFrame(root)
    root.mainloop()
    from tkinter import *
import smbus

RED_LED   = 0b00000001
GREEN_LED = 0b00000010
BLUE_LED  = 0b00000100

class MainFrame(Frame):

    def __init__(self, master):
        master.title('LED Control Example')
        master.geometry("400x240+10+10")

        redLedOnButton = Button(master, background="RED", text="RED LED ON",
                                command=lambda: self.onButtonClickEvent(0))
        redLedOnButton.pack(expand=1)

        redLedOffButton = Button(master, background="RED", text="RED LED OFF",
                                 command=lambda: self.onButtonClickEvent(1))
        redLedOffButton.pack(expand=1)

        greenLedOnButton = Button(master, background="GREEN", text="GREEN LED ON",
                                  command=lambda: self.onButtonClickEvent(2))
        greenLedOnButton.pack(expand=1)

        greenLedOffButton = Button(master, background="GREEN", text="GREEN LED OFF",
                                   command=lambda: self.onButtonClickEvent(3))
        greenLedOffButton.pack(expand=1)

        blueLedOnButton = Button(master, background="BLUE", text="BLUE LED ON",
                                 command=lambda: self.onButtonClickEvent(4))
        blueLedOnButton.pack(expand=1)

        blueLedOffButton = Button(master, background="BLUE", text="BLUE LED OFF",
                                  command=lambda: self.onButtonClickEvent(5))
        blueLedOffButton.pack(expand=1)

        self.ledInit()

    def onButtonClickEvent(self, pin):
        if pin == 0:
            self.ledOn(RED_LED)
        elif pin == 1:
            self.ledOff(RED_LED)
        elif pin == 2:
            self.ledOn(GREEN_LED)
        elif pin == 3:
            self.ledOff(GREEN_LED)
        elif pin == 4:
            self.ledOn(BLUE_LED)
        elif pin == 5:
            self.ledOff(BLUE_LED)

    def ledInit(self):
        self.state = 0b00000000
        self.bus = smbus.SMBus(1)

    def ledOn(self, cmd):
        self.state = (self.state | cmd)
        self.bus.write_byte(0x20, self.state)

    def ledOff(self, cmd):
        self.state = (self.state & (~cmd))
        self.bus.write_byte(0x20, self.state)

if __name__ == '__main__':
    root = Tk()
    mainFrame = MainFrame(root)
    root.mainloop()
    sys.exit()