import guizero
import sys
filewrite = open("script.py", "w")
filewrite.write("import time\n")
filewrite.write("import gpiozero\n")

#windows
mainwindow = guizero.App(title = "gpguio", width = 640, height = 480)
LEDwindow = guizero.Window(mainwindow, width = 640, height = 480)
LEDwindow.hide()
Sleepwindow = guizero.Window(mainwindow, width = 640, height = 480)
Sleepwindow.hide()
Powerwindow = guizero.Window(mainwindow, width = 640, height = 480)
Powerwindow.hide()

def LEDwindowexit():
    LEDnamebox.clear()
    LEDpinnumberbox.clear()
    LEDwindow.hide()
def updateLEDname():
    LEDname = LEDnamebox.value
    LEDpinnumber = LEDpinnumberbox.value
    filewrite.write(str(LEDname) + " = LED(" + str(LEDpinnumber) + ")\n")
    LEDnamebox.clear()
    LEDpinnumberbox.clear()
    LEDwindow.hide()
    actiontext = guizero.Text(mainwindow, text = "Added LED with name " + str(LEDname) + " at GPIO pin " + str(LEDpinnumber))
def updatePoweractions():
    Sleeptime = Sleeptimebox.value
    filewrite.write("time.sleep(" + str(Sleeptime) + ")\n" )
    Sleeptimebox.clear()
    Sleepwindow.hide()
    actiontext = guizero.Text(mainwindow, text = "Added sleep timer for "+ str(Sleeptime) + " seconds",)

#buttons
#mainwindow
LEDselectbutton = guizero.PushButton(mainwindow, command = LEDwindow.show, text = "New LED")
Sleepwindowbutton = guizero.PushButton(mainwindow, command = Sleepwindow.show, text = "Add Sleep Timer")
Powerwindowbutton = guizero.PushButton(mainwindow, command = Sleepwindow.show, text = "Power Controls")
mainwindowexitbutton = guizero.PushButton(mainwindow, command = mainwindow.destroy, text = "Exit", align = "bottom")
#LEDwindow
LEDselectexitbutton = guizero.PushButton(LEDwindow, command = LEDwindowexit, text = "Cancel", align = "bottom")
LEDnameconfirmbutton = guizero.PushButton(LEDwindow, command = updateLEDname, text = "Confirm LED selection", align = "top")

#Sleepwindow
Sleeptimeconfirmbutton = guizero.PushButton(Sleepwindow, command = updatePoweractions, text = "Confirm Sleep Timer")

#user input fields
LEDnametext = guizero.Text(LEDwindow, text="\nLED name (can be anything)")
LEDnamebox = guizero.TextBox(LEDwindow)
LEDpinnumbertext = guizero.Text(LEDwindow, text = "\nGPIO pin number to which LED is connected.\nShould be any number from 1 to 40")
LEDpinnumberbox = guizero.TextBox(LEDwindow)
Sleeptimetext = guizero.Text(Sleepwindow, text = "Sleep time (in seconds)")
Sleeptimebox = guizero.TextBox(Sleepwindow)
#End of file
mainwindow.display()
filewrite.close()
sys.exit()


