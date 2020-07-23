import guizero
import sys
import time
filewrite = open("script.py", "w")
filewrite.write("import time\n")
filewrite.write("import gpiozero\n")

#windows
mainwindow = guizero.App(title = "gpguio by arnitdo", width = 720, height = 540)
mainwindow.hide()
mainwindow.disable()
LEDwindow = guizero.Window(mainwindow, width = 720, height = 540, title = "New LED")
LEDwindow.hide()
LEDwindow.disable()
PWMLEDwindow = guizero.Window(mainwindow, width = 720, height = 540, title = "New PWM LED")
PWMLEDwindow.hide()
PWMLEDwindow.disable()
Sleepwindow = guizero.Window(mainwindow, width = 720, height = 540, title = "Add Sleep Timer")
Sleepwindow.hide()
Sleepwindow.disable()
LEDcontrolwindow = guizero.Window(mainwindow, width = 720, height = 540, title = "LED controls")
LEDcontrolwindow.hide()
LEDcontrolwindow.disable()
PWMLEDcontrolwindow = guizero.Window(mainwindow, width = 720, height = 540, title = "PWMLED controls")
PWMLEDcontrolwindow.hide()
PWMLEDcontrolwindow.disable()
Buttonwindow  = guizero.Window(mainwindow, width = 720, height = 540, title = "New Button")
Buttonwindow.hide()
Buttonwindow.disable()
Buttoncontrolwindow = guizero.Window(mainwindow, width = 720, height = 540, title = "Button controls")
Buttoncontrolwindow.hide()
Buttoncontrolwindow.disable()
#Will add later
#Printwindow = guizero.Window(mainwindow, width = 720, height = 540, title = "Print")
#Printwindow.hide()
#ASAP
Disclaimerwindow = guizero.Window(mainwindow, width = 720, height = 540, title = "Disclaimer")
exitappwindow = guizero.Window(mainwindow, width = 240, height = 120, title = "Exit App")
exitappwindow.hide()
exitappwindow.disable()

#Function definitions are in no particular order
def exitapppopup():
    exitappwindow.show()

def Buttoncontrolconfirmaction():
    #This is going to be big...turns out not!
    if Buttoncontrolbuttonselect.value == None or Buttoncontrolbuttonactionselect.value ==None or ButtoncontrolLEDselect.value == None or ButtoncontrolLEDactionselect.value == None:
        Nobuttonselecttext = guizero.Text(Buttoncontrolwindow, text = "No selection made. Try again")
    else:
        if Buttoncontrolbuttonactionselect.value == "when pressed":
            if ButtoncontrolLEDactionselect.value == "Turn ON":
                filewrite.write(str(Buttoncontrolbuttonselect.value) + ".when_pressed = " + str(ButtoncontrolLEDselect.value) + ".on()\n")
            elif ButtoncontrolLEDactionselect.value == "Turn OFF":
                filewrite.write(str(Buttoncontrolbuttonselect.value) + ".when_pressed = " + str(ButtoncontrolLEDselect.value) + ".off()\n")
            else:
                pass
        Buttoncontrolwindow.hide()
def updateButtonname():
    Buttonname = Buttonnamebox.value
    Buttonpinnumber = Buttonpinnumberbox.value
    if Buttonnamebox.value != "" and Buttonpinnumberbox.value != "":
        Buttoncontrolbuttonselect.append(str(Buttonname))
        Buttonnamebox.clear
        Buttonwindow.hide()
        Actionlog.append("Added Button with name " + str(Buttonname) + " at GPIO pin " + str(Buttonpinnumber))
    else:
        NoButtonwarntext = guizero.Text(Buttonwindow, text = "Invalid input", align = "top")
def Buttonwindowexit():
    Buttonnamebox.clear()
    Buttonpinnumberbox.clear()
    Buttonwindow.hide()

def LEDwindowexit():
    LEDnamebox.clear()
    LEDpinnumberbox.clear()
    LEDwindow.hide()

def updateLEDname():
    if LEDnamebox.value != "" and (LEDpinnumberbox.value != "" and int(LEDpinnumberbox.value) > 0 and int(LEDpinnumberbox.value) < 41):
        LEDpowerselect.append(str(LEDnamebox.value))
        ButtoncontrolLEDselect.append(str(LEDnamebox.value))
        filewrite.write(str(LEDnamebox.value) + " = LED(" + str(LEDpinnumberbox.value) + ")\n")
        LEDnamebox.clear()
        LEDpinnumberbox.clear()
        LEDwindow.hide()
        Actionlog.append("Added LED with name " + str(LEDnamebox.value) + " at GPIO pin " + str(LEDpinnumberbox.value))
    else:
        NoLEDwarntext = guizero.Text(LEDwindow, text = "Invalid input", align = "top")
def PWMLEDwindowexit():
    PWMLEDnamebox.clear()
    PWMLEDpinnumberbox.clear()
    PWMLEDwindow.hide()

def updatePWMLEDname():
    if PWMLEDnamebox.value != "" and (PWMLEDpinnumberbox.value != "" and int(PWMLEDpinnumberbox.value) < 41 and int(PWMLEDpinnumber.value) > 0):
        PWMLEDpowerselect.append(str(PWMLEDnamebox.value))
        filewrite.write(str(PWMLEDnamebox.value) + " = PWMLED(" + str(PWMLEDpinnumberbox.value) + ")\n")
        PWMLEDnamebox.clear()
        PWMLEDpinnumberbox.clear()
        PWMLEDwindow.hide()
        Actionlog.append("Added PWMLED with name " + str(PWMLEDnamebox.value) + " at GPIO pin " + str(PWMLEDpinnumberbox.value))
    else:
        NoPWMLEDwarntext = guizero.Text(PWMLEDwindow, text = "Invalid input", align = "top")
def PWMLEDcontrolbrightness():
    if ((PWMLEDpowerselect.value !=None ) and (PWMbrightinputbox.value != "")):
        PWMbrightinput = float(PWMbrightinputbox.value)
        filewrite.write("#Runs for 10 seconds by defaut\npwmsecondcounter = 0\nwhile pwmsecondcounter in range(0,10):\n    pwmsecondcounter = pwmsecondcounter + 1\n    time.sleep(1)\n"+ "    " + str(PWMLEDpowerselect.value) + ".value = " + str(PWMbrightinput) + "\n    #Add more custom code or change the duration of the while() loop if you want")
        #added a permanent while loop. More functionality later :-)
        Actionlog.append("PWMLED " + str(PWMLEDpowerselect.value) + " brightness set to " + str(PWMbrightinput))
        PWMLEDcontrolwindow.hide()
    elif PWMLEDpowerselect.value == None:
        NoLEDselect = guizero.Text(PWMLEDcontrolwindow, text = "Invalid selection", align = "top")
    else:
        pass
def updateSleeptime():
    if Sleeptimebox.value != "":
        Sleeptime = Sleeptimebox.value
        filewrite.write("time.sleep(" + str(Sleeptime) + ")\n" )
        Sleeptimebox.clear()
        Sleepwindow.hide()
        Actionlog.append("Added sleep timer for "+ str(Sleeptime) + " seconds")
    else:
        NoSleepinputtext = guizero.Text(Sleepwindow, text = "Invalid input")
def Sleeptimeexit():
    Sleeptimebox.clear()
    Sleepwindow.hide()

def LEDpowerON():
    if LEDpowerselect.value != None:
        filewrite.write(str(LEDpowerselect.value) + ".on()\n")
        LEDcontrolwindow.hide()
    else:
        pass
    if LEDpowerselect.value == None:
        NoLEDselect = guizero.Text(LEDcontrolwindow, text = "Invalid selection", align = "top")
    else:
        Actionlog.append("LED " + str(LEDpowerselect.value) + " will turn ON")

def LEDpowerOFF():
    if LEDpowerselect.value != None:
        filewrite.write(str(LEDpowerselect.value) + ".off()\n")
        LEDcontrolwindow.hide()
        Actionlog.append("LED " + str(LEDpowerselect.value) + " will turn OFF")
    else:
        NoLEDselect = guizero.Text(LEDcontrolwindow, text = "Invalid selection", align = "top")

def Disclaimeraccept():
    Disclaimerwindow.destroy()
    mainwindow.enable()
    mainwindow.show()
    LEDwindow.enable()
    PWMLEDwindow.enable()
    LEDcontrolwindow.enable()
    PWMLEDcontrolwindow.enable()
    Sleepwindow.enable()
    Buttonwindow.enable()
    Buttoncontrolwindow.enable()
    exitappwindow.enable()

def Disclaimerdecline():
    Disclaimerwindow.destroy()
    mainwindow.destroy()

#All widgets based on window

#Disclaimerwindow
Disclaimerdeclinebutton = guizero.PushButton(Disclaimerwindow, command = Disclaimerdecline, text = "Exit", align = "bottom", padx = 38)
Disclaimeracceptbutton = guizero.PushButton(Disclaimerwindow, command = Disclaimeraccept, text = "I understand", align = "bottom")
Disclaimertext1 = guizero.Text(Disclaimerwindow, text = "The creator of this program is not responsible for :\n1)Damage caused to electrical components\n2)Harm caused to the user by electrical components\n3)Loss of functionality of electrical components\n")
Disclaimertext2 = guizero.Text(Disclaimerwindow, text = "Note that the program does not interact with any components\nIt merely creates code which the user can run at their own risk\n")
Disclaimertext3 = guizero.Text(Disclaimerwindow, text = "Program made by arnitdo\ngithub.com/arnitdo")

#Buttonwindow
Buttonnametext = guizero.Text(Buttonwindow, text = "\nName of new Button")
Buttonnamebox = guizero.TextBox(Buttonwindow)
Buttonpinnumbertext = guizero.Text(Buttonwindow, text = "\nPin to which button is connedted")
Buttonpinnumberbox = guizero.TextBox(Buttonwindow)
Buttonselectexitbutton = guizero.PushButton(Buttonwindow, command = Buttonwindowexit, text = "Cancel", align = "bottom", padx = 14)
Buttonnameconfirmbutton = guizero.PushButton(Buttonwindow, command = updateButtonname, text = "Confirm", align = "bottom")

#Buttoncontrolwindow
Buttoncontrolbuttonselect = guizero.ListBox(Buttoncontrolwindow, items = [], scrollbar = True, height = 100, width = 150, align = "top")
Buttoncontrolbuttonactionselect = guizero.ListBox(Buttoncontrolwindow, items = ["when pressed", "when released"], scrollbar = True, height = 100, width = 150, align = "top")
ButtoncontrolLEDselect = guizero.ListBox(Buttoncontrolwindow, items = [], scrollbar = True, height = 100, width = 150, align = "top")
ButtoncontrolLEDactionselect = guizero.ListBox(Buttoncontrolwindow, items = ["Turn ON", "Turn OFF"], height = 100, width = 150,  align = "top",scrollbar = True)
Buttoncontrolcancelactionbutton = guizero.PushButton(Buttoncontrolwindow, command = Buttoncontrolwindow.hide, text = "Cancel", padx = 8, align = "bottom")
Buttoncontrolconfirmactionbutton = guizero.PushButton(Buttoncontrolwindow, command = Buttoncontrolconfirmaction, text = "Confirm", align = "bottom", padx = 5)

#mainwindow

LEDselectbutton = guizero.PushButton(mainwindow, command = LEDwindow.show, text = "New LED", padx = 39)
LEDcontrolwindowbutton = guizero.PushButton(mainwindow, command = LEDcontrolwindow.show, text = "LED Controls", padx = 26)
PWMLEDselectbutton = guizero.PushButton(mainwindow, command = PWMLEDwindow.show, text = "New PWMLED", padx = 22)
PWMLEDcontrolwindowbutton = guizero.PushButton(mainwindow, command = PWMLEDcontrolwindow.show, text = "PWMLED Controls", padx = 10)
Buttonwindowbutton = guizero.PushButton(mainwindow, command = Buttonwindow.show, text = "New Button", padx = 30)
Buttoncontrolwindowbutton = guizero.PushButton(mainwindow, command = Buttoncontrolwindow.show, text = "Button Controls", padx = 17)
Sleepwindowbutton = guizero.PushButton(mainwindow, command = Sleepwindow.show, text = "Add Sleep Timer", padx = 14)
mainwindowexitbutton = guizero.PushButton(mainwindow, command = exitapppopup, text = "Save and Quit", align = "top", padx = 22)
Actionlogtext = guizero.Text(mainwindow, text = "\nLog :")
Actionlog = guizero.ListBox(mainwindow, items = [], scrollbar = True, height = 150, width = 400)
#LEDwindow

LEDselectexitbutton = guizero.PushButton(LEDwindow, command = LEDwindowexit, text = "Cancel", align = "bottom", padx = 14)
LEDnameconfirmbutton = guizero.PushButton(LEDwindow, command = updateLEDname, text = "Confirm", align = "bottom")

#PWM LED WINDOW
PWMLEDselectexitbutton = guizero.PushButton(PWMLEDwindow, command = PWMLEDwindowexit, text = "Cancel", align = "bottom", padx = 14)
PWMLEDnameconfirmbutton = guizero.PushButton(PWMLEDwindow, command = updatePWMLEDname, text = "Confirm", align = "bottom")
#Sleepwindow

Sleeptimeexitbutton = guizero.PushButton(Sleepwindow, command = Sleeptimeexit, text = "Cancel", align = "bottom", padx = 55)
Sleeptimeconfirmbutton = guizero.PushButton(Sleepwindow, command = updateSleeptime, text = "Confirm Sleep Timer", align ="bottom")

#LEDcontrolwindow
LEDPowertext = guizero.Text(LEDcontrolwindow, text = "Power ON / OFF LEDs.\nSelect LED from dropdown list.\nLEDs must be created first using the \nNew LED option in the main window")
LEDpowerselect = guizero.ListBox(LEDcontrolwindow, items = [], scrollbar = True, height = 150, width = 150)
PowerONbutton =  guizero.PushButton(LEDcontrolwindow, text = "Turn Selected LED ON", align = "top", command = LEDpowerON, padx = 13)
PowerOFFbutton =  guizero.PushButton(LEDcontrolwindow, text = "Turn Selected LED OFF", align = "top", command = LEDpowerOFF)
LEDcontrolwindowexitbutton = guizero.PushButton(LEDcontrolwindow, text = "Cancel", command = LEDcontrolwindow.hide, align = "top", padx = 62)

#PWMLEDcontrolwindow
PWMLEDPowertext = guizero.Text(PWMLEDcontrolwindow, text = "Control PWM LEDS.\nSelect LED from dropdown list.\nPWMLEDs must be created first using the \nNew PWMLED option in the main window")
PWMLEDpowerselect = guizero.ListBox(PWMLEDcontrolwindow, items = [], scrollbar = True, height = 150, width = 150)
PWMLEDbrighttext = guizero.Text(PWMLEDcontrolwindow, text = "Set PWM brightness\nMin value = 0 (OFF)\nMax value = 1 (Full Brightness)\nInput any decimal value from 0 to 1\nNote: PWMLED brightness time is set to 10 seconds by default\nTo modify it, make necessary changes to the script.py file")
PWMbrightinputbox = guizero.TextBox(PWMLEDcontrolwindow)
PWMLEDcontrolwindowexitbutton = guizero.PushButton(PWMLEDcontrolwindow, text = "Cancel", command = PWMLEDcontrolwindow.hide, align = "bottom", padx = 15)
PWMLEDbrightconfirmbutton = guizero.PushButton(PWMLEDcontrolwindow, command = PWMLEDcontrolbrightness, text = "Confirm", align = "bottom")

#user input fields

LEDnametext = guizero.Text(LEDwindow, text="\nLED name (can be anything reasonable)")
LEDnamebox = guizero.TextBox(LEDwindow)
LEDpinnumbertext = guizero.Text(LEDwindow, text = "\nPhysical pin number to which LED is connected.\nShould be any number from 1 to 40\nSee pinout.xyz for more info or\nrun command pinout on your raspberry pi")
LEDpinnumberbox = guizero.TextBox(LEDwindow)
PWMLEDnametext = guizero.Text(PWMLEDwindow, text="\nPWMLED name (can be anything reasonable)")
PWMLEDnamebox = guizero.TextBox(PWMLEDwindow)
PWMLEDpinnumbertext = guizero.Text(PWMLEDwindow, text = "\nPhysical pin number to which PWMLED is connected.\nShould be any number from 1 to 40\nSee pinout.xyz for more info or\nrun command pinout on your raspberry pi")
PWMLEDpinnumberbox = guizero.TextBox(PWMLEDwindow)
Sleeptimetext = guizero.Text(Sleepwindow, text = "\nSleep time (in seconds)")
Sleeptimebox = guizero.TextBox(Sleepwindow)


#Exit app popup
exitappwindowtext = guizero.Text(exitappwindow, text = "Thank you for using gpguio\nFile saved as script.py")
exitappconfirm = guizero.PushButton(exitappwindow, command = mainwindow.destroy, text = "OK", align = "bottom", padx = 20)
#End of file

mainwindow.display()
filewrite.close()
sys.exit()