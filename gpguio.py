import guizero
import sys
import time
filewrite = open("script.py", "w")
filewrite.write("import time\n")
filewrite.write("from gpiozero import *\n") #Not pep8 compliant. alternatively can add gpiozero.<component> = <componenttype>(<pinnumber>)
#But I feel that importing * is better  due to large amounts of component functions that are going to be added later
filewrite.write("from sense_hat import SenseHat\n")
filewrite.write("from picamera import PiCamera\n")
filewrite.write("from signal import pause\n")
filewrite.write("sensehat = SenseHat()\n")
filewrite.write("camera = PiCamera()\n")

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
Morecomponentswindow = guizero.Window(mainwindow, width = 720, height = 540, title = "More Components")
Morecomponentswindow.hide()
Morecomponentswindow.disable()
Morecomponentswindow.hide()
SenseHatmatrixcustomtextwindow = guizero.Window(mainwindow, width = 720, height = 540, title = "SenseHat custom text")
SenseHatmatrixcustomtextwindow.hide()
SenseHatmatrixcustomtextwindow.disable()
SenseHatmatrixcustomiconwindow = guizero.Window(mainwindow, width = 720, height = 540, title = "SenseHat custom icon", layout = "grid")
SenseHatmatrixcustomiconwindow.hide()
SenseHatmatrixcustomiconwindow.disable()
Picamerawindow = guizero.Window(mainwindow, width = 720, height = 540, title = "PiCamera Capture")
Picamerawindow.hide()
Picamerawindow.disable()
LEDBoardwindow = guizero.Window(mainwindow, width = 720, height = 540, title = "LED Board")
LEDBoardwindow.hide()
LEDBoardwindow.disable()
Disclaimerwindow = guizero.Window(mainwindow, width = 720, height = 540, title = "Disclaimer")
exitappwindow = guizero.Window(mainwindow, width = 240, height = 120, title = "Exit App")
exitappwindow.hide()
exitappwindow.disable()

#Function definitions are in no particular order
def exitapppopup():
    exitappwindow.show()

def Fileappendcolors():
    filewrite.write("V = [148, 0, 211]\n")
    filewrite.write("I = [75, 0 , 130]\n")
    filewrite.write("B = [0, 0, 255]\n")
    filewrite.write("G = [0, 255, 0]\n")
    filewrite.write("Y = [255, 255, 0]\n")
    filewrite.write("O = [255, 127, 0]\n")
    filewrite.write("R = [255, 0, 0]\n")
    filewrite.write("W = [255, 255, 255]\n")
    filewrite.write("K = [0, 0, 0]\n")

def Buttoncontrolconfirmaction():
    #This is going to be big...turns out not!
    if Buttoncontrolbuttonselect.value == None or Buttoncontrolbuttonactionselect.value ==None or ButtoncontrolLEDselect.value == None or ButtoncontrolLEDactionselect.value == None:
        Nobuttonselecttext = guizero.Text(Buttoncontrolwindow, text = "No selection made. Try again")
    else:
        if Buttoncontrolbuttonactionselect.value == "when pressed":
            if ButtoncontrolLEDactionselect.value == "Turn ON":
                filewrite.write(str(Buttoncontrolbuttonselect.value) + ".when_pressed = " + str(ButtoncontrolLEDselect.value) + ".on()\n")
                Actionlog.append("LED " + str(ButtoncontrolLEDselect.value) + " will turn ON when button " + str(Buttoncontrolbuttonselect.value) + " is pressed")
            elif ButtoncontrolLEDactionselect.value == "Turn OFF":
                filewrite.write(str(Buttoncontrolbuttonselect.value) + ".when_pressed = " + str(ButtoncontrolLEDselect.value) + ".off()\n")
                Actionlog.append("LED " + str(ButtoncontrolLEDselect.value) + " will turn OFF when button " + str(Buttoncontrolbuttonselect.value) + " is pressed")
            else:
                pass
        elif Buttoncontrolbuttonactionselect.value == "when released":
            if ButtoncontrolLEDactionselect.value == "Turn ON":
                filewrite.write(str(Buttoncontrolbuttonselect.value) + ".when_released = " + str(ButtoncontrolLEDselect.value) + ".on()\n")
                Actionlog.append("LED " + str(ButtoncontrolLEDselect.value) + " will turn ON when button " + str(Buttoncontrolbuttonselect.value) + " is released")
            elif ButtoncontrolLEDactionselect.value == "Turn OFF":
                filewrite.write(str(Buttoncontrolbuttonselect.value) + ".when_released = " + str(ButtoncontrolLEDselect.value) + ".off()\n")
                Actionlog.append("LED " + str(ButtoncontrolLEDselect.value) + " will turn OFF when button " + str(Buttoncontrolbuttonselect.value) + " is released")
            else:
                pass
        Buttoncontrolwindow.hide()
def updateButtonname():
    Buttonname = Buttonnamebox.value
    Buttonpinnumber = Buttonpinnumberbox.value
    if Buttonnamebox.value != "" and Buttonpinnumberbox.value != "":
        Buttoncontrolbuttonselect.append(str(Buttonname))
        Buttonnamebox.clear()
        Buttonpinnumberbox.clear()
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
        LEDBoardselect.append(str(LEDpinnumberbox.value))
        filewrite.write(str(LEDnamebox.value) + " = LED(" + str(LEDpinnumberbox.value) + ")\n")
        Actionlog.append("Added LED with name " + str(LEDnamebox.value) + " at GPIO pin " + str(LEDpinnumberbox.value))
        LEDnamebox.clear()
        LEDpinnumberbox.clear()
        LEDwindow.hide()
    else:
        NoLEDwarntext = guizero.Text(LEDwindow, text = "Invalid input", align = "top")
def PWMLEDwindowexit():
    PWMLEDnamebox.clear()
    PWMLEDpinnumberbox.clear()
    PWMLEDwindow.hide()

def updatePWMLEDname():
    if PWMLEDnamebox.value != "" and (PWMLEDpinnumberbox.value != "" and int(PWMLEDpinnumberbox.value) < 41 and int(PWMLEDpinnumberbox.value) > 0):
        PWMLEDpowerselect.append(str(PWMLEDnamebox.value))
        filewrite.write(str(PWMLEDnamebox.value) + " = PWMLED(" + str(PWMLEDpinnumberbox.value) + ")\n")
        Actionlog.append("Added PWMLED with name " + str(PWMLEDnamebox.value) + " at GPIO pin " + str(PWMLEDpinnumberbox.value))
        PWMLEDnamebox.clear()
        PWMLEDpinnumberbox.clear()
        PWMLEDwindow.hide()
    else:
        NoPWMLEDwarntext = guizero.Text(PWMLEDwindow, text = "Invalid input", align = "top")
def PWMLEDcontrolbrightness():
    if ((PWMLEDpowerselect.value !=None ) and (PWMbrightinputbox.value != "")):
        PWMbrightinput = float(PWMbrightinputbox.value)
        filewrite.write(str(PWMLEDpowerselect.value) + ".value = " + str(PWMbrightinput) + "\ntime.sleep(10)\n" + str(PWMLEDpowerselect.value) + ".value = 0")
        #10 second brightness timer. Can be changed by user
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
        Morecomponentswindow.hide()
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
    Morecomponentswindow.enable()
    SenseHatmatrixcustomtextwindow.enable()
    SenseHatmatrixcustomiconwindow.enable()
    Picamerawindow.enable()
    Fileappendcolors()

def Vflipsensematrix():
    filewrite.write("sensehat.flip_v()\n")
    Actionlog.append("SenseHat matrix display flipped vertically")
    Sensematrixvflippedtext = guizero.Text(SenseHatmatrixcustomtextwindow, text = "SenseHat matrix display flipped vertically")

def Hflipsensematrix():
    filewrite.write("sensehat.flip_h()\n")
    Actionlog.append("SenseHat matrix display flipped horizontally")
    Sensematrixhflippedtext = guizero.Text(SenseHatmatrixcustomtextwindow, text = "SenseHat matrix display flipped horizontally")


def Picameraconfirmcapture():
    if Picamerawindowfilebox.value != "":
        filewrite.write("time.sleep(5) # Camera warm up time, is necessary\ncamera.capture(\"" + str(Picamerawindowfilebox.value) + "\")\n")
        Actionlog.append("PiCamera will capture image " + str(Picamerawindowfilebox.value))
        Picamerawindowfilebox.clear()
        Picamerawindow.hide()
        Morecomponentswindow.hide()
    else:
        Invalidimagename = guizero.Text(Picamerawindow, text = "Invalid Input", align = "bottom")
        Picamerawindowfilebox.clear()

def Picameracancelcapture():
    Picamerawindowfilebox.clear()
    Picamerawindow.hide()

def CancelSenseHattext():
    SenseHatmatrixcustomtextbox.clear()
    SenseHatmatrixcustomtextsenserotationbox.clear()
    SenseHatmatrixcustomtextwindow.hide()
    Morecomponentswindow.hide()

def ConfirmSenseHattext():
    validrotationlist = ["0","90","180","270"]
    if SenseHatmatrixcustomtextbox.value != "" and SenseHatmatrixcustomtextsenserotationbox.value in validrotationlist:
        filewrite.write("sensehat.set_rotation(" + str(SenseHatmatrixcustomtextsenserotationbox.value) + ")\n")
        filewrite.write("sensehat.show_message(\""+ str(SenseHatmatrixcustomtextbox.value) + "\")\n")
        Actionlog.append("SenseHat will be rotated " + str(SenseHatmatrixcustomtextsenserotationbox.value) + " degrees")
        Actionlog.append("SenseHat will display text " + str(SenseHatmatrixcustomtextbox.value))
        SenseHatmatrixcustomtextwindow.hide()
        SenseHatmatrixcustomtextbox.clear()
        Morecomponentswindow.hide()
    else:
        Invalidcustomtextinputtext = guizero.Text(SenseHatmatrixcustomtextwindow, text = "Invalid Input")

def CancelSenseHaticon():
    for mled in SenseHarmatrixmledlist:
        mled.clear()
    SenseHatmatrixcustomiconwindow.hide()

def ConfirmSenseHaticon():
    mledscanner = 0
    for mled in SenseHarmatrixmledlist:
        if mled.value in SenseHatmatrixcustomiconvalidinputslist:
            mledscanner = mledscanner + 1
            if mledscanner == 64:
                filewrite.write("icon = [\n")
                filewrite.write("   " + str(mled1x1.value) + ", " + str(mled2x1.value) + ", " + str(mled3x1.value) + ", " + str(mled4x1.value) + ", " + str(mled5x1.value) + ", " + str(mled6x1.value) + ", " + str(mled7x1.value) + ", " + str(mled8x1.value) + ", \n")
                filewrite.write("   " + str(mled1x2.value) + ", " + str(mled2x2.value) + ", " + str(mled3x2.value) + ", " + str(mled4x2.value) + ", " + str(mled5x2.value) + ", " + str(mled6x2.value) + ", " + str(mled7x2.value) + ", " + str(mled8x2.value) + ", \n")
                filewrite.write("   " + str(mled1x3.value) + ", " + str(mled2x3.value) + ", " + str(mled3x3.value) + ", " + str(mled4x3.value) + ", " + str(mled5x3.value) + ", " + str(mled6x3.value) + ", " + str(mled7x3.value) + ", " + str(mled8x3.value) + ", \n")
                filewrite.write("   " + str(mled1x4.value) + ", " + str(mled2x4.value) + ", " + str(mled3x4.value) + ", " + str(mled4x4.value) + ", " + str(mled5x4.value) + ", " + str(mled6x4.value) + ", " + str(mled7x4.value) + ", " + str(mled8x4.value) + ", \n")
                filewrite.write("   " + str(mled1x5.value) + ", " + str(mled2x5.value) + ", " + str(mled3x5.value) + ", " + str(mled4x5.value) + ", " + str(mled5x5.value) + ", " + str(mled6x5.value) + ", " + str(mled7x5.value) + ", " + str(mled8x5.value) + ", \n")
                filewrite.write("   " + str(mled1x6.value) + ", " + str(mled2x6.value) + ", " + str(mled3x6.value) + ", " + str(mled4x6.value) + ", " + str(mled5x6.value) + ", " + str(mled6x6.value) + ", " + str(mled7x6.value) + ", " + str(mled8x6.value) + ", \n")
                filewrite.write("   " + str(mled1x7.value) + ", " + str(mled2x7.value) + ", " + str(mled3x7.value) + ", " + str(mled4x7.value) + ", " + str(mled5x7.value) + ", " + str(mled6x7.value) + ", " + str(mled7x7.value) + ", " + str(mled8x7.value) + ", \n")
                filewrite.write("   " + str(mled1x8.value) + ", " + str(mled2x8.value) + ", " + str(mled3x8.value) + ", " + str(mled4x8.value) + ", " + str(mled5x8.value) + ", " + str(mled6x8.value) + ", " + str(mled7x8.value) + ", " + str(mled8x8.value) + "\n")
                filewrite.write("]\n\n")#Double \n for making it pretty!!
                filewrite.write("sensehat.set_pixels(icon)\n")
                mled.clear()
                SenseHatmatrixcustomiconwindow.hide()
                Actionlog.append("SenseHat matrix will display custom icon\n")
            else:
                pass
    else:
        Invalidiconinputtext = guizero.Text(SenseHatmatrixcustomiconwindow, text = "Invalid Input", grid = [10,12], align = "bottom")

def LEDBoardexit():
    LEDBoardwindow.hide()
    LEDBoardnamebox.clear()

def updateLEDBoard():
    if LEDBoardnamebox.value != "" and LEDBoardselect.value != None:
        ledstring = "" #Sets the led string to "". each led pin is added to the string
        for traverser in LEDBoardselect.value[0 : -1]:
            ledstring = ledstring + traverser + ", "
        ledstring = ledstring + LEDBoardselect.value[-1]
        filewrite.write(str(LEDBoardnamebox.value) + " = LEDBoard(" + ledstring + ")\n") #the string of LED pins is added to the file after LEDBoard = (
        Actionlog.append("Created LEDBoard with LEDs at pins " + str(LEDBoardselect.value))
        ButtoncontrolLEDselect.append(str(LEDBoardnamebox.value))
        LEDpowerselect.append(str(LEDBoardnamebox.value))
        LEDBoardnamebox.clear()
        LEDBoardwindow.hide()
    else:
        InvalidLEDBoardtext = guizero.Text(LEDBoardwindow, text = "Invalid Input", align = "bottom")

def LEDBoardexit():
    LEDBoardnamebox.clear()
    LEDBoardwindow.hide()

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
Buttoncontrolhelptext = guizero.Text(Buttoncontrolwindow, text = "Interface with LEDs using Buttons here\nSelect Button from first list\nSelect trigger from second list\nSelect LED to interact with in third list\nSelect LED power option in the fourth list\nNote that Buttons and LEDs need to be created / defined first" )
Buttoncontrolbuttonselect = guizero.ListBox(Buttoncontrolwindow, items = [], scrollbar = True, height = 75, width = 150, align = "top")
Buttoncontrolbuttonactionselect = guizero.ListBox(Buttoncontrolwindow, items = ["when pressed", "when released"], scrollbar = True, height = 75, width = 150, align = "top")
ButtoncontrolLEDselect = guizero.ListBox(Buttoncontrolwindow, items = [], scrollbar = True, height = 75, width = 150, align = "top")
ButtoncontrolLEDactionselect = guizero.ListBox(Buttoncontrolwindow, items = ["Turn ON", "Turn OFF"], height = 75, width = 150,  align = "top",scrollbar = True)
Buttoncontrolcancelactionbutton = guizero.PushButton(Buttoncontrolwindow, command = Buttoncontrolwindow.hide, text = "Cancel", padx = 10, align = "bottom")
Buttoncontrolconfirmactionbutton = guizero.PushButton(Buttoncontrolwindow, command = Buttoncontrolconfirmaction, text = "Confirm", align = "bottom", padx = 6)

#mainwindow

LEDselectbutton = guizero.PushButton(mainwindow, command = LEDwindow.show, text = "New LED", padx = 39)
LEDcontrolwindowbutton = guizero.PushButton(mainwindow, command = LEDcontrolwindow.show, text = "LED Controls", padx = 26)
PWMLEDselectbutton = guizero.PushButton(mainwindow, command = PWMLEDwindow.show, text = "New PWMLED", padx = 22)
PWMLEDcontrolwindowbutton = guizero.PushButton(mainwindow, command = PWMLEDcontrolwindow.show, text = "PWMLED Controls", padx = 10)
Buttonwindowbutton = guizero.PushButton(mainwindow, command = Buttonwindow.show, text = "New Button", padx = 30)
Buttoncontrolwindowbutton = guizero.PushButton(mainwindow, command = Buttoncontrolwindow.show, text = "Button Controls", padx = 17)
Morecomponentswindowbutton = guizero.PushButton(mainwindow, command = Morecomponentswindow.show, text = "More Components", padx = 8)
mainwindowexitbutton = guizero.PushButton(mainwindow, command = exitapppopup, text = "Save and Quit", align = "top", padx = 22)
Actionlogtext = guizero.Text(mainwindow, text = "\nLog :")
Actionlog = guizero.ListBox(mainwindow, items = [], scrollbar = True, height = 150, width = 400)

#Morecomponentswindow
LEDBoardwindowbutton =  guizero.PushButton(Morecomponentswindow, command = LEDBoardwindow.show, text = "LED Board", padx = 50)
Sleepwindowbutton = guizero.PushButton(Morecomponentswindow, command = Sleepwindow.show, text = "Add Sleep Timer", padx = 30)
SenseHatmatrixcustomtextwindowbutton = guizero.PushButton(Morecomponentswindow, command = SenseHatmatrixcustomtextwindow.show, text = "Custom SenseHat Text")
SenseHatmatrixcustomiconwindwowbutton = guizero.PushButton(Morecomponentswindow, command = SenseHatmatrixcustomiconwindow.show, text = "Custom SenseHat Icon", padx = 11)
Picamerawindowbutton = guizero.PushButton(Morecomponentswindow, command  = Picamerawindow.show, text = "PiCamera Image Capture", padx = 2)
Morecomponentswindowcancelbutton = guizero.PushButton(Morecomponentswindow, command = Morecomponentswindow.hide, text = "Cancel", padx = 63)

#LEDwindow

LEDselectexitbutton = guizero.PushButton(LEDwindow, command = LEDwindowexit, text = "Cancel", align = "bottom", padx = 14)
LEDnameconfirmbutton = guizero.PushButton(LEDwindow, command = updateLEDname, text = "Confirm", align = "bottom")

#PWM LED WINDOW
PWMLEDselectexitbutton = guizero.PushButton(PWMLEDwindow, command = PWMLEDwindowexit, text = "Cancel", align = "bottom", padx = 14)
PWMLEDnameconfirmbutton = guizero.PushButton(PWMLEDwindow, command = updatePWMLEDname, text = "Confirm", align = "bottom")

#LEDBoardwindow
LEDBoardnametext = guizero.Text(LEDBoardwindow, text = "\nSet the name for the LED Board\nLED Boards can be controlled\nunder LED Controls window\n")
LEDBoardnamebox = guizero.TextBox(LEDBoardwindow)
LEDBoardLEDselecttext = guizero.Text(LEDBoardwindow, text = "\nSelect LED pins to add to LED Board\nDefine LEDs in the New LED window\n")
LEDBoardselect = guizero.ListBox(LEDBoardwindow, multiselect = True, scrollbar = True, items = [])
LEDBoardexitbutton = guizero.PushButton(LEDBoardwindow, command = LEDBoardexit, text = "Cancel", align = "bottom", padx = 14)
LEDBoardconfirmbutton = guizero.PushButton(LEDBoardwindow, command = updateLEDBoard, text = "Confirm", align = "bottom")
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

#SenseHatmatrixcustomtextwindowbuttons
SenseHatmatrixcustomtexthelptext = guizero.Text(SenseHatmatrixcustomtextwindow, text = "Input text to display on LED matrix")
SenseHatmatrixcustomtextbox = guizero.TextBox(SenseHatmatrixcustomtextwindow)
SenseHatmatrixcustomtextsenserotationtext = guizero.Text(SenseHatmatrixcustomtextwindow, text = "\nSet SenseHat rotation\nAccepted values 0,90,180 and 270")
SenseHatmatrixcustomtextsenserotationbox = guizero.TextBox(SenseHatmatrixcustomtextwindow, text = "0")
SenseHatmatrixcustomtextsensefliptext = guizero.Text(SenseHatmatrixcustomtextwindow, text = "Select whether you want to rotate the displayed text\n")
SenseHatmatrixcustomtextvflipbutton = guizero.PushButton(SenseHatmatrixcustomtextwindow, command = Vflipsensematrix, text = "Flip text vertically", padx =18)
SenseHatmatrixcustomtexthflipbutton = guizero.PushButton(SenseHatmatrixcustomtextwindow, command = Hflipsensematrix, text = "Flip text horizontally")
SenseHatmatrixcustomtextcancelbutton = guizero.PushButton(SenseHatmatrixcustomtextwindow, command = CancelSenseHattext, text = "Cancel", align = "bottom",padx = 14)
SenseHatmatrixcustomtextconfirmbutton = guizero.PushButton(SenseHatmatrixcustomtextwindow, command = ConfirmSenseHattext, text = "Confirm", align = "bottom")

#Picamerawindowtext
Picamerawindowtext = guizero.Text(Picamerawindow, text = "\nInput file name for PiCamera Image Capture\nThis can also be a filepath which includes directories\n")
Picamerawindowconfirmbutton = guizero.PushButton(Picamerawindow, command = Picameracancelcapture, text = "Cancel", padx = 14, align = "bottom")
Picamerawindowconfirmbutton = guizero.PushButton(Picamerawindow, command = Picameraconfirmcapture, text = "Confirm", align = "bottom")


#user input fields
#LEDwindowboxes
LEDnametext = guizero.Text(LEDwindow, text="\nLED name (can be anything reasonable)")
LEDnamebox = guizero.TextBox(LEDwindow)
LEDpinnumbertext = guizero.Text(LEDwindow, text = "\nPhysical pin number to which LED is connected.\nShould be any number from 1 to 40\nSee pinout.xyz for more info or\nrun command pinout on your raspberry pi")
LEDpinnumberbox = guizero.TextBox(LEDwindow)

#PWMLEDwindowboxes
PWMLEDnametext = guizero.Text(PWMLEDwindow, text="\nPWMLED name (can be anything reasonable)")
PWMLEDnamebox = guizero.TextBox(PWMLEDwindow)
PWMLEDpinnumbertext = guizero.Text(PWMLEDwindow, text = "\nPhysical pin number to which PWMLED is connected.\nShould be any number from 1 to 40\nSee pinout.xyz for more info or\nrun command pinout on your raspberry pi")
PWMLEDpinnumberbox = guizero.TextBox(PWMLEDwindow)

#Sleepwindowboxes
Sleeptimetext = guizero.Text(Sleepwindow, text = "\nSleep time (in seconds)")
Sleeptimebox = guizero.TextBox(Sleepwindow)

#Picamerawindowboxes
Picamerawindowfilebox = guizero.TextBox(Picamerawindow, text = "capture.jpg", width = 15)

#Exit app popup
exitappwindowtext = guizero.Text(exitappwindow, text = "Thank you for using gpguio\nFile saved as script.py")
exitappconfirm = guizero.PushButton(exitappwindow, command = mainwindow.destroy, text = "OK", align = "bottom", padx = 20)

#SenseHatmatrixcustomiconwindowboxes
blanktextforcentering = guizero.Text(SenseHatmatrixcustomiconwindow, text = "                                   ", grid = [0,0,1,10])#Because the mled matrix is offset to the left, this should bring it to center
SenseHatmatrixcustomiconwindowhelptext = guizero.Text(SenseHatmatrixcustomiconwindow, text = "\nInput colors to be displayed on matrix\nAvailable color selection :\nFor violet [148, 0, 211] input V\nFor indigo [75, 0, 130] input I\nFor blue [0, 0, 255] input B\nFor green [0, 255, 0] input G\nFor yellow [255, 255, 0] input Y\nFor orange [255, 127, 0] input O\nFor red [255,0,0] input R\nFor white [255, 255, 255] input W\nFor black (off) [0, 0, 0] input K\nNote that inputs are case sensitive\nThe values you input will reflect on the matrix\n", align = "top", grid = [1,0,8,1])
SenseHatmatrixcustomiconvalidinputslist = ["V", "I", "B", "G", "Y", "O", "R", "W", "K"]
#Is there any alternative to this ? If so, please recommend
mled1x1 = guizero.TextBox(SenseHatmatrixcustomiconwindow, grid = [1,1], width = 6, align = "top")
mled2x1 = guizero.TextBox(SenseHatmatrixcustomiconwindow, grid = [2,1], width = 6, align = "top")
mled3x1 = guizero.TextBox(SenseHatmatrixcustomiconwindow, grid = [3,1], width = 6, align = "top")
mled4x1 = guizero.TextBox(SenseHatmatrixcustomiconwindow, grid = [4,1], width = 6, align = "top")
mled5x1 = guizero.TextBox(SenseHatmatrixcustomiconwindow, grid = [5,1], width = 6, align = "top")
mled6x1 = guizero.TextBox(SenseHatmatrixcustomiconwindow, grid = [6,1], width = 6, align = "top")
mled7x1 = guizero.TextBox(SenseHatmatrixcustomiconwindow, grid = [7,1], width = 6, align = "top")
mled8x1 = guizero.TextBox(SenseHatmatrixcustomiconwindow, grid = [8,1], width = 6, align = "top")
mled1x2 = guizero.TextBox(SenseHatmatrixcustomiconwindow, grid = [1,2], width = 6, align = "top")
mled2x2 = guizero.TextBox(SenseHatmatrixcustomiconwindow, grid = [2,2], width = 6, align = "top")
mled3x2 = guizero.TextBox(SenseHatmatrixcustomiconwindow, grid = [3,2], width = 6, align = "top")
mled4x2 = guizero.TextBox(SenseHatmatrixcustomiconwindow, grid = [4,2], width = 6, align = "top")
mled5x2 = guizero.TextBox(SenseHatmatrixcustomiconwindow, grid = [5,2], width = 6, align = "top")
mled6x2 = guizero.TextBox(SenseHatmatrixcustomiconwindow, grid = [6,2], width = 6, align = "top")
mled7x2 = guizero.TextBox(SenseHatmatrixcustomiconwindow, grid = [7,2], width = 6, align = "top")
mled8x2 = guizero.TextBox(SenseHatmatrixcustomiconwindow, grid = [8,2], width = 6, align = "top")
mled1x3 = guizero.TextBox(SenseHatmatrixcustomiconwindow, grid = [1,3], width = 6, align = "top")
mled2x3 = guizero.TextBox(SenseHatmatrixcustomiconwindow, grid = [2,3], width = 6, align = "top")
mled3x3 = guizero.TextBox(SenseHatmatrixcustomiconwindow, grid = [3,3], width = 6, align = "top")
mled4x3 = guizero.TextBox(SenseHatmatrixcustomiconwindow, grid = [4,3], width = 6, align = "top")
mled5x3 = guizero.TextBox(SenseHatmatrixcustomiconwindow, grid = [5,3], width = 6, align = "top")
mled6x3 = guizero.TextBox(SenseHatmatrixcustomiconwindow, grid = [6,3], width = 6, align = "top")
mled7x3 = guizero.TextBox(SenseHatmatrixcustomiconwindow, grid = [7,3], width = 6, align = "top")
mled8x3 = guizero.TextBox(SenseHatmatrixcustomiconwindow, grid = [8,3], width = 6, align = "top")
mled1x4 = guizero.TextBox(SenseHatmatrixcustomiconwindow, grid = [1,4], width = 6, align = "top")
mled2x4 = guizero.TextBox(SenseHatmatrixcustomiconwindow, grid = [2,4], width = 6, align = "top")
mled3x4 = guizero.TextBox(SenseHatmatrixcustomiconwindow, grid = [3,4], width = 6, align = "top")
mled4x4 = guizero.TextBox(SenseHatmatrixcustomiconwindow, grid = [4,4], width = 6, align = "top")
mled5x4 = guizero.TextBox(SenseHatmatrixcustomiconwindow, grid = [5,4], width = 6, align = "top")
mled6x4 = guizero.TextBox(SenseHatmatrixcustomiconwindow, grid = [6,4], width = 6, align = "top")
mled7x4 = guizero.TextBox(SenseHatmatrixcustomiconwindow, grid = [7,4], width = 6, align = "top")
mled8x4 = guizero.TextBox(SenseHatmatrixcustomiconwindow, grid = [8,4], width = 6, align = "top")
mled1x5 = guizero.TextBox(SenseHatmatrixcustomiconwindow, grid = [1,5], width = 6, align = "top")
mled2x5 = guizero.TextBox(SenseHatmatrixcustomiconwindow, grid = [2,5], width = 6, align = "top")
mled3x5 = guizero.TextBox(SenseHatmatrixcustomiconwindow, grid = [3,5], width = 6, align = "top")
mled4x5 = guizero.TextBox(SenseHatmatrixcustomiconwindow, grid = [4,5], width = 6, align = "top")
mled5x5 = guizero.TextBox(SenseHatmatrixcustomiconwindow, grid = [5,5], width = 6, align = "top")
mled6x5 = guizero.TextBox(SenseHatmatrixcustomiconwindow, grid = [6,5], width = 6, align = "top")
mled7x5 = guizero.TextBox(SenseHatmatrixcustomiconwindow, grid = [7,5], width = 6, align = "top")
mled8x5 = guizero.TextBox(SenseHatmatrixcustomiconwindow, grid = [8,5], width = 6, align = "top")
mled1x6 = guizero.TextBox(SenseHatmatrixcustomiconwindow, grid = [1,6], width = 6, align = "top")
mled2x6 = guizero.TextBox(SenseHatmatrixcustomiconwindow, grid = [2,6], width = 6, align = "top")
mled3x6 = guizero.TextBox(SenseHatmatrixcustomiconwindow, grid = [3,6], width = 6, align = "top")
mled4x6 = guizero.TextBox(SenseHatmatrixcustomiconwindow, grid = [4,6], width = 6, align = "top")
mled5x6 = guizero.TextBox(SenseHatmatrixcustomiconwindow, grid = [5,6], width = 6, align = "top")
mled6x6 = guizero.TextBox(SenseHatmatrixcustomiconwindow, grid = [6,6], width = 6, align = "top")
mled7x6 = guizero.TextBox(SenseHatmatrixcustomiconwindow, grid = [7,6], width = 6, align = "top")
mled8x6 = guizero.TextBox(SenseHatmatrixcustomiconwindow, grid = [8,6], width = 6, align = "top")
mled1x7 = guizero.TextBox(SenseHatmatrixcustomiconwindow, grid = [1,7], width = 6, align = "top")
mled2x7 = guizero.TextBox(SenseHatmatrixcustomiconwindow, grid = [2,7], width = 6, align = "top")
mled3x7 = guizero.TextBox(SenseHatmatrixcustomiconwindow, grid = [3,7], width = 6, align = "top")
mled4x7 = guizero.TextBox(SenseHatmatrixcustomiconwindow, grid = [4,7], width = 6, align = "top")
mled5x7 = guizero.TextBox(SenseHatmatrixcustomiconwindow, grid = [5,7], width = 6, align = "top")
mled6x7 = guizero.TextBox(SenseHatmatrixcustomiconwindow, grid = [6,7], width = 6, align = "top")
mled7x7 = guizero.TextBox(SenseHatmatrixcustomiconwindow, grid = [7,7], width = 6, align = "top")
mled8x7 = guizero.TextBox(SenseHatmatrixcustomiconwindow, grid = [8,7], width = 6, align = "top")
mled1x8 = guizero.TextBox(SenseHatmatrixcustomiconwindow, grid = [1,8], width = 6, align = "top")
mled2x8 = guizero.TextBox(SenseHatmatrixcustomiconwindow, grid = [2,8], width = 6, align = "top")
mled3x8 = guizero.TextBox(SenseHatmatrixcustomiconwindow, grid = [3,8], width = 6, align = "top")
mled4x8 = guizero.TextBox(SenseHatmatrixcustomiconwindow, grid = [4,8], width = 6, align = "top")
mled5x8 = guizero.TextBox(SenseHatmatrixcustomiconwindow, grid = [5,8], width = 6, align = "top")
mled6x8 = guizero.TextBox(SenseHatmatrixcustomiconwindow, grid = [6,8], width = 6, align = "top")
mled7x8 = guizero.TextBox(SenseHatmatrixcustomiconwindow, grid = [7,8], width = 6, align = "top")
mled8x8 = guizero.TextBox(SenseHatmatrixcustomiconwindow, grid = [8,8], width = 6, align = "top")

SenseHarmatrixmledlist = [mled1x1, mled2x1, mled3x1, mled4x1, mled5x1, mled6x1, mled7x1, mled8x1, mled1x2, mled2x2, mled3x2, mled4x2, mled5x2, mled6x2, mled7x2, mled8x2, mled1x3, mled2x3, mled3x3, mled4x3, mled5x3, mled6x3, mled7x3, mled8x3, mled1x4, mled2x4, mled3x4, mled4x4, mled5x4, mled6x4, mled7x4, mled8x4, mled1x5, mled2x5, mled3x5, mled4x5, mled5x5, mled6x5, mled7x5, mled8x5, mled1x6, mled2x6, mled3x6, mled4x6, mled5x6, mled6x6, mled7x6, mled8x6, mled1x7, mled2x7, mled3x7, mled4x7, mled5x7, mled6x7, mled7x7, mled8x7, mled1x8, mled2x8, mled3x8, mled4x8, mled5x8, mled6x8, mled7x8, mled8x8]
SenseHatmatrixcustomiconcancelbutton = guizero.PushButton(SenseHatmatrixcustomiconwindow, command = CancelSenseHaticon, text = "Cancel", padx = 14, grid = [4,11,2,1], align = "bottom")
SenseHatmatrixcustomiconconfirmbutton = guizero.PushButton(SenseHatmatrixcustomiconwindow, command = ConfirmSenseHaticon, text = "Confirm", grid = [4,10,2,1], align = "bottom")

#End of file

mainwindow.display()
filewrite.write("pause()\n")
filewrite.close()
sys.exit()