import guizero
import sys
import time
filewrite = open("script.py", "w")
filewrite.write("import time\n")
filewrite.write("import gpiozero\n")

#windows
mainwindow = guizero.App(title = "gpguio by arnitdo", width = 640, height = 480)
mainwindow.hide()
LEDwindow = guizero.Window(mainwindow, width = 640, height = 480, title = "New LED")
LEDwindow.hide()
Sleepwindow = guizero.Window(mainwindow, width = 640, height = 480, title = "Add Sleep Timer")
Sleepwindow.hide()
Powerwindow = guizero.Window(mainwindow, width = 640, height = 480, title = "Power Controls")
Powerwindow.hide()
Disclaimerwindow = guizero.Window(mainwindow, width = 640, height = 480, title = "Disclaimer")
exitappwindow = guizero.Window(mainwindow, width = 240, height = 120, title = "Exit App")
exitappwindow.hide()
def exitapppopup():
    exitappwindow.show()

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
    Actionlog.append("Added LED with name " + str(LEDname) + " at GPIO pin " + str(LEDpinnumber))

def updateSleeptime():
    Sleeptime = Sleeptimebox.value
    filewrite.write("time.sleep(" + str(Sleeptime) + ")\n" )
    Sleeptimebox.clear()
    Sleepwindow.hide()
    Actionlog.append("Added sleep timer for "+ str(Sleeptime) + " seconds")

def Sleeptimeexit():
    Sleeptimebox.clear()
    Sleepwindow.hide()

def LEDpowerON():
    if LEDpowerselect.value != None:
        filewrite.write(str(LEDpowerselect.value) + ".on()\n")
        Powerwindow.hide()
    else:
        pass
    if LEDpowerselect.value == None:
        NoLEDselect = guizero.Text(Powerwindow, text = "No LED selected", align = "top")
    else:
        Actionlog.append("LED " + str(LEDpowerselect.value) + " will turn ON")

def LEDpowerOFF():
    if LEDpowerselect.value != None:
        filewrite.write(str(LEDpowerselect.value) + ".on()\n")
        Powerwindow.hide()
    else:
        pass
    if LEDpowerselect.value == None:
        NoLEDselect = guizero.Text(Powerwindow, text = "No LED selected", align = "top")
    else:
        Actionlog.append("LED " + str(LEDpowerselect.value) + " will turn OFF")

def Disclaimeraccept():
    Disclaimerwindow.destroy()
    mainwindow.show()

def Disclaimerdecline():
    Disclaimerwindow.destroy()
    mainwindow.destroy()

#buttons

#Disclaimerwindow
Disclaimerdeclinebutton = guizero.PushButton(Disclaimerwindow, command = Disclaimerdecline, text = "Exit", align = "bottom", padx = 38)
Disclaimeracceptbutton = guizero.PushButton(Disclaimerwindow, command = Disclaimeraccept, text = "I understand", align = "bottom")
Disclaimertext1 = guizero.Text(Disclaimerwindow, text = "The creator of this program is not responsible for :\n1)Damage caused to electrical components\n2)Harm caused to the user by electrical components\n3)Loss of functionality of electrical components\n")
Disclaimertext2 = guizero.Text(Disclaimerwindow, text = "Note that the program does not interact with any components\nIt merely creates code which the user can run at their own risk\n")
Disclaimertext3 = guizero.Text(Disclaimerwindow, text = "Program made by arnitdo\ngithub.com/arnitdo")

#mainwindow

LEDselectbutton = guizero.PushButton(mainwindow, command = LEDwindow.show, text = "New LED", padx = 35)
Sleepwindowbutton = guizero.PushButton(mainwindow, command = Sleepwindow.show, text = "Add Sleep Timer")
Powerwindowbutton = guizero.PushButton(mainwindow, command = Powerwindow.show, text = "Power Controls", padx = 15)
mainwindowexitbutton = guizero.PushButton(mainwindow, command = exitapppopup, text = "Save and Quit", align = "top", padx = 18)
Actionlogtext = guizero.Text(mainwindow, text = "\nLog :")
Actionlog = guizero.ListBox(mainwindow, items = [], scrollbar = True, height = 150, width = 300)
#LEDwindow

LEDselectexitbutton = guizero.PushButton(LEDwindow, command = LEDwindowexit, text = "Cancel", align = "bottom", padx = 14)
LEDnameconfirmbutton = guizero.PushButton(LEDwindow, command = updateLEDname, text = "Confirm", align = "bottom")
#Sleepwindow

Sleeptimeconfirmbutton = guizero.PushButton(Sleepwindow, command = updateSleeptime, text = "Confirm Sleep Timer", align ="bottom")
Sleeptimeexitbutton = guizero.PushButton(Sleepwindow, command = Sleeptimeexit, text = "Cancel", align = "bottom", padx = 55)

#Powerwindow
Powertext = guizero.Text(Powerwindow, text = "Power ON / OFF LEDs.\nSelect LED from dropdown list.\nLEDs must be created first using the \nNew LED option in the main window")
LEDpowerselect = guizero.ListBox(Powerwindow, items = [], scrollbar = True, height = 150, width = 150)
PowerONbutton =  guizero.PushButton(Powerwindow, text = "Turn Selected LED ON", align = "top", command = LEDpowerON, padx = 13)
PowerOFFbutton =  guizero.PushButton(Powerwindow, text = "Turn Selected LED OFF", align = "top", command = LEDpowerOFF)
Powerwindowexitbutton = guizero.PushButton(Powerwindow, text = "Cancel", command = Powerwindow.hide, align = "top", padx = 62)
#user input fields

LEDnametext = guizero.Text(LEDwindow, text="\nLED name (can be anything reasonable)")
LEDnamebox = guizero.TextBox(LEDwindow)
LEDpinnumbertext = guizero.Text(LEDwindow, text = "\nPhysical pin number to which LED is connected.\nShould be any number from 1 to 40\nSee pinout.xyz for more info or\nrun command pinout on your raspberry pi")
LEDpinnumberbox = guizero.TextBox(LEDwindow)
Sleeptimetext = guizero.Text(Sleepwindow, text = "Sleep time (in seconds)")
Sleeptimebox = guizero.TextBox(Sleepwindow)

#Exit app popup
exitappwindowtext = guizero.Text(exitappwindow, text = "Thank you for using gpguio\nFile saved as script.py")
exitappconfirm = guizero.PushButton(exitappwindow, command = mainwindow.destroy, text = "OK", align = "bottom", padx = 20)
#End of file

mainwindow.display()
filewrite.close()
sys.exit()