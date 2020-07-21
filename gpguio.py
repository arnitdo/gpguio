import guizero
filewrite = open("script.py", "w")
filewrite.write("import time\n")
filewrite.write("import gpiozero\n")
#windows
mainwindow = guizero.App()
LEDwindow = guizero.Window(mainwindow)
LEDwindow.hide()

def updateLEDname():
    LEDname = LEDnamebox.value
    LEDpinnumber = LEDpinnumberbox.value
    filewrite.write(str(LEDname) + " = LED(" + str(LEDpinnumber) + ")\n")
    LEDnamebox.clear
    LEDpinnumberbox.clear
    LEDwindow.hide()


#buttons
#mainwindow
LEDselectbutton = guizero.PushButton(mainwindow, command = LEDwindow.show, text = "New LED")
mainwindowexitbutton = guizero.PushButton(mainwindow, command = mainwindow.destroy, text = "Exit")
#LEDwindow
LEDselectexitbutton = guizero.PushButton(LEDwindow, command = LEDwindow.hide, text = "Cancel")
LEDnameconfirmbutton = guizero.PushButton(LEDwindow, command = updateLEDname, text = "Confirm LED selection")

#user input fields
LEDnamebox = guizero.TextBox(LEDwindow)
LEDpinnumberbox = guizero.TextBox(LEDwindow)

#End of file
mainwindow.display()
filewrite.close()
os.exit()

