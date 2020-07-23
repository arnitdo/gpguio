**How-to-run:**

Download the gpguio.py file from the repo or from the release file

Ensure dependencies are satisfied (see below)

Run gpguio.py

After you have finished, click Save and Quit.

A file named script.py will be created which will contain code as per user actions

Run script.py on a Raspberry Pi with the appropriate components installed as per user actions


**Dependencies :**

python3, guizero and tkinter

tkinter comes installed with python installations in Windows and Mac (if option selected during installation)

for tkinter(LINUX ONLY) run - sudo apt install python3-tk
  
for guizero(ALL OS) run - pip3 install guizero


**Welcome to gpguio**

gpguio is a GUI tool for basic GPIO usage


_What does gpguizero do?_

See **features** 


_What hardware does it require?_

Well, any working device with the above listed dependencies satisfied. That's it.


_What is it supposed to do?_

Get user inputs and pipe relevant python code to a file (script.py)
See **How to run** above


**Features**

Add LED devices on a certain GPIO pin

Turn ON / OFF LED devices

Add PWM LED devices on a certain GPIO pin

Change PWM LED device brightness

Add sleep timers

Add buttons.

Interface with LEDs (Non PWM as of now) such as:

  Turn ON when button is pressed

  Turn OFF when button is pressed

A log to see which actions made by the user

That is it for now!

**Planned features -**

Buzzer interfacing

PiCamera interfacing

LEDBoard functionality

LEDBarGraph functionality

Full RGB LED functionality
