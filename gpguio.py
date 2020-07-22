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
    LEDpowerselect.append(str(LEDname))
    filewrite.write(str(LEDname) + " = LED(" + str(LEDpinnumber) + ")\n")
    LEDnamebox.clear()
    LEDpinnumberbox.clear()
    LEDwindow.hide()
    actiontext = guizero.Text(mainwindow, text = "Added LED with name " + str(LEDname) + " at GPIO pin " + str(LEDpinnumber))

def updateSleeptime():
    Sleeptime = Sleeptimebox.value
    filewrite.write("time.sleep(" + str(Sleeptime) + ")\n" )
    Sleeptimebox.clear()
    Sleepwindow.hide()
    actiontext = guizero.Text(mainwindow, text = "Added sleep timer for "+ str(Sleeptime) + " seconds",)

def Sleeptimeexit():
    Sleeptimebox.clear()
    Sleepwindow.hide()

def LEDpowerON():
    if LEDpowerselect.value != None:
        filewrite.write(str(LEDpowerselect.value) + ".on()\n")
        Powerwindow.hide
    else:
        pass
    if LEDpowerselect.value == None:
        NoLEDselect = guizero.Text(Powerwindow, text = "No LED selected", align = "top")
    else:
        actiontext = guizero.Text(mainwindow, text = "LED " + str(LEDpowerselect.value) + " will turn ON")

def LEDpowerOFF():
    if LEDpowerselect.value != None:
        filewrite.write(str(LEDpowerselect.value) + ".on()\n")
        Powerwindow.hide
    else:
        pass
    if LEDpowerselect.value == None:
        NoLEDselect = guizero.Text(Powerwindow, text = "No LED selected", align = "top")
    else:
        actiontext = guizero.Text(mainwindow, text = "LED " + str(LEDpowerselect.value) + " will turn ON")


#buttons

#mainwindow

LEDselectbutton = guizero.PushButton(mainwindow, command = LEDwindow.show, text = "New LED", padx = 35)
Sleepwindowbutton = guizero.PushButton(mainwindow, command = Sleepwindow.show, text = "Add Sleep Timer")
Powerwindowbutton = guizero.PushButton(mainwindow, command = Powerwindow.show, text = "Power Controls", padx = 15)
mainwindowexitbutton = guizero.PushButton(mainwindow, command = mainwindow.destroy, text = "Exit", align = "bottom")

#LEDwindow

LEDselectexitbutton = guizero.PushButton(LEDwindow, command = LEDwindowexit, text = "Cancel", align = "bottom")
LEDnameconfirmbutton = guizero.PushButton(LEDwindow, command = updateLEDname, text = "Confirm LED selection", align = "top")
#Sleepwindow

Sleeptimeconfirmbutton = guizero.PushButton(Sleepwindow, command = updateSleeptime, text = "Confirm Sleep Timer")
Sleeptimeexitbutton = guizero.PushButton(Sleepwindow, command = Sleeptimeexit, text = "Cancel", align = "bottom")

#Powerwindow
Powertext = guizero.Text(Powerwindow, text = "Power ON / OFF LEDs.\nSelect LED from dropdown list.\nLEDs must be created first using the \nNew LED option in the main window")
LEDpowerselect = guizero.ListBox(Powerwindow, items = [], scrollbar = True)
Powerwindowexitbutton = guizero.PushButton(Powerwindow, text = "Cancel", align = "bottom", command = Powerwindow.hide)
PowerONbutton =  guizero.PushButton(Powerwindow, text = "Turn Selected LED ON", align = "top", command = LEDpowerON)
PowerOFFbutton =  guizero.PushButton(Powerwindow, text = "Turn Selected LED OFF", align = "top", command = LEDpowerOFF)
#user input fields

LEDnametext = guizero.Text(LEDwindow, text="\nLED name (can be anything)")
LEDnamebox = guizero.TextBox(LEDwindow)
LEDpinnumbertext = guizero.Text(LEDwindow, text = "\nPhysical pin number to which LED is connected.\nShould be any number from 1 to 40\nSee pinout.xyz for more info OR\nrun command pinout on your raspberry pi")
LEDpinnumberbox = guizero.TextBox(LEDwindow)
Sleeptimetext = guizero.Text(Sleepwindow, text = "Sleep time (in seconds)")
Sleeptimebox = guizero.TextBox(Sleepwindow)

#End of file

mainwindow.display()
filewrite.close()
sys.exit()
