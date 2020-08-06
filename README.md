**Please send feedback in the Feedback and Discussion thread, under issues tab**

**Release 1.2.1 may be the final release of gpguio. If any additional functionality is absolutely needed, please contact me.**

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

Display Custom Text on SenseHat

Display custom icon on SenseHat

Define LED boards, as well as interact with them using buttons

Picamera image capture

A log to see which actions made by the user

That is it for now!

**Planned features -**

SenseHAT custom images - DONE!

Buzzer interfacing - Put on hold

PiCamera interfacing - DONE!

LEDBoard functionality - DONE!

LEDBarGraph functionality - Put on hold

Full RGB LED functionality - Put on hold

Put on hold indicates that the functionality may or may not be added, please request, if you want it to be added.


**Interface images, for those interested**

![Basic Interface](https://user-images.githubusercontent.com/68515826/88478558-163e8a80-cf67-11ea-9bbf-268ca0fe1b36.png)
The main interface window
![LED window](https://user-images.githubusercontent.com/68515826/88478651-b1cffb00-cf67-11ea-83a5-56776dce61ea.png)
The LED creation / definition window
![PWM LED controls](https://user-images.githubusercontent.com/68515826/88478672-d88e3180-cf67-11ea-9d16-0adc9768e144.png)
PWM LED brightness control window
![SenseHat Custom Text](https://user-images.githubusercontent.com/68515826/88478724-3589e780-cf68-11ea-8a34-a34414ce262d.png)
Custom Text on SenseHat matrix window
And much more on the way!
