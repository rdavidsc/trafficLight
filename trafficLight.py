from gpiozero import LED
from gpiozero import Button
from time import sleep

rLed = LED(17)
yLed = LED(27)
gLed = LED(22)
pLed = LED(23)
button = Button(16)

buttonPressed = False
greenCounter = 16


def pedestrianPressed():
    global buttonPressed
    if(not buttonPressed):
        pLed.on()
        buttonPressed = True
        print("A pedestrian has pressed the button")


def stopCicle():
    print("Stop cicle")
    global buttonPressed
    # Yellow light
    yLed.on()
    gLed.off()
    sleep(10)
    yLed.blink(0.8,0.2)
    sleep(10)
    # Red light - Pedestrian should pass now
    rLed.on()
    yLed.off()
    pLed.blink(0.8,0.2)
    sleep(30)
    rLed.off()
    pLed.off()
    buttonPressed = False    
    
def greenCicle():
    #Green light
    gLed.on()
    sleep(20)
    
button.when_pressed = pedestrianPressed
#    pedestrianPressed()
# button.when_released = pLed.off()   


while True:
    if(buttonPressed):
        greenCounter = 0
        stopCicle()        
    else:
        greenCounter += 1
        print('Counter: ',greenCounter, buttonPressed)
        if(greenCounter > 15):
            greenCounter = 0
            stopCicle()
        else:
            greenCicle()

            
        
        
        
        
        
        
        
