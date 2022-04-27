import tkinter
import RPi.GPIO as GPIO

GREEN = 7
BLUE = 8
RED = 10
ledGroup = 0
GPIO.setmode(GPIO.BOARD)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)
GPIO.setup(RED, GPIO.OUT)


def redToggle():
    GPIO.output(BLUE, GPIO.LOW)
    GPIO.output(GREEN, GPIO.LOW)
    GPIO.output(RED, GPIO.HIGH)


def blueToggle():
    GPIO.output(BLUE, GPIO.HIGH)
    GPIO.output(GREEN, GPIO.LOW)
    GPIO.output(RED, GPIO.LOW)


def greenToggle():
    GPIO.output(BLUE, GPIO.LOW)
    GPIO.output(GREEN, GPIO.HIGH)
    GPIO.output(RED, GPIO.LOW)


window = tkinter.Tk()
window.title("RGB LED Switch")

redRadioButton = tkinter.Radiobutton(window, text="Red LED", command=redToggle, height=1, width=20, variable=ledGroup, value=RED)
blueRadioButton = tkinter.Radiobutton(window, text="Blue LED", command=blueToggle, height=1, width=20, variable=ledGroup, value=BLUE)
greenRadioButton = tkinter.Radiobutton(window, text="Green LED", command=greenToggle, height=1, width=20, variable=ledGroup, value=GREEN)

redRadioButton.grid(row=0, column=1)
blueRadioButton.grid(row=1, column=1)
greenRadioButton.grid(row=2, column=1)

window.protocol("WM_DELETE_WINDOW")

window.mainloop()
