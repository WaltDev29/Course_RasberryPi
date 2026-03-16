from tkinter import *
import RPi.GPIO as GPIO
import time
import threading

MOTOR_P = 19
MOTOR_M = 13

state = ""

class MainFrame(Frame):
    def __init__(self, master):
        master.title('DC Motor Control Example')
        master.geometry("400x240+10+10")
        dcmotorthread = threading.Thread(target=self.dc_motor_thread)
        dcmotorthread.start()

        button = []

        button.append( Button(master, background="cyan", text= "Clockwise",
                              command=lambda:self.onButtonClickEvent(0)) )
        button[0].pack(side=LEFT, expand = 1)

        button.append( Button(master, background="cyan", text= "STOP",
                              command=lambda:self.onButtonClickEvent(1)) )
        button[1].pack(side=LEFT, expand = 1)

        button.append( Button(master, background="cyan", text= "Count Clockwise",
                              command=lambda:self.onButtonClickEvent(2)) )
        button[2].pack(side=LEFT, expand = 1)
        
    def onButtonClickEvent(self,pin):
        global state
        if(pin == 0) :
            state = 'CW'
        elif(pin == 1) :
            state = 'STOP'
        elif(pin == 2) :
            state = 'CCW'
    
    def dc_motor_thread(self) :
        try :
            while(True):
                if state == 'CW' :
                    GPIO.output(MOTOR_P,GPIO.HIGH)
                    GPIO.output(MOTOR_M,GPIO.LOW)
                elif state == 'STOP':
                    GPIO.output(MOTOR_P,GPIO.LOW)
                    GPIO.output(MOTOR_M,GPIO.LOW)
                elif state == 'CCW':
                    GPIO.output(MOTOR_P,GPIO.LOW)
                    GPIO.output(MOTOR_M,GPIO.HIGH)
                time.sleep(0.1)
        except : 
            time.sleep(1)

def gpio_dcMotor_init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
        
    GPIO.setup(MOTOR_P,GPIO.OUT)
    GPIO.setup(MOTOR_M,GPIO.OUT)

    GPIO.output(MOTOR_P, GPIO.LOW)
    GPIO.output(MOTOR_M, GPIO.LOW)
        
def gpio_dcMotor_cleanup():
    GPIO.output(MOTOR_P, GPIO.LOW)
    GPIO.output(MOTOR_M, GPIO.LOW)
    GPIO.cleanup()

if (__name__ == '__main__'):
    gpio_dcMotor_init()
    root = Tk()
    mainFrame = MainFrame(root)
    root.mainloop()
    gpio_dcMotor_cleanup()
    sys.exit()