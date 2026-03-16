from tkinter import *
import smbus
RED_LED   = 0b00000001
class MainFrame(Frame):
    def __init__(self, master):
        master.title('LED Control Example')
        master.geometry("400x240+10+10")

        # RED LED ON 
        redLedOnButton = Button(master, background="RED", text= "RED LED ON",command=lambda:self.onButtonClickEvent(0))
        redLedOnButton.pack(side=LEFT, expand = 1)

        # RED LED OFF
        redLedOffButton = Button(master, background="RED", text= "RED LED OFF", command=lambda:self.onButtonClickEvent(1))
        redLedOffButton.pack(side=LEFT, expand = 1)

        self.ledInit()
    def onButtonClickEvent(self,pin):
        if(pin == 0) :
            self.ledOn(RED_LED)

        elif(pin == 1) :
            self.ledOff(RED_LED)

    def ledInit(self):
        self.state = 0b00000000
        self.bus = smbus.SMBus(1)

    def ledOn(self,cmd):
        self.state = (self.state | cmd)
        self.bus.write_byte(0x20, self.state)   

    def ledOff(self,cmd):
        self.state = (self.state & (~cmd)) 
        self.bus.write_byte(0x20, self.state)

if (__name__ == '__main__'):
    root = Tk()
    mainFrame = MainFrame(root)
    root.mainloop()
    sys.exit()