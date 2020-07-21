#imports
import guizero
#import gpiozero
filewrite = open("script.py", "w")

def LEDwindowshow():
    LEDwindow.show()
mainwindow = guizero.App()
LEDwindow = guizero.Window(mainwindow)
LEDwindow.hide()

def killLEDwindow():
    LEDwindow.hide()
LEDselectbutton = guizero.PushButton(mainwindow, command = LEDwindowshow, args = None, text = "New LED")
LEDselectexitbutton = guizero.PushButton(LEDwindow, command = killLEDwindow, args = None, text = "Exit")

mainwindow.display()
filewrite.close()

