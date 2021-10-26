# MagTag Stock Tracker / Ticker 

The MagTag Stock Tracker / Ticker is an Adafruit MagTag Stock Tracker with a gorgeous ePaper / eInk display. It uses WiFi onboard to get the latest stock information for display with deep sleep. It saves battery and keeps the previous stock price saved before sleeping. Also, it includes logic for recovery from a reboot or dead battery. Also, checks the battery and warns when a battery is low from an audible tone.


<img width="640" alt="MagTag Stock" src="https://user-images.githubusercontent.com/1426877/138564465-26fa4e60-e6bd-473e-8613-862aef786c7a.JPG"> 



It flashes green or red based the change of the stock price.

https://user-images.githubusercontent.com/1426877/138565675-b1f6193a-10d9-42c1-83f8-92c0dc441e15.mov

Learned a bunch about Deep Sleep with CircuitPython https://learn.adafruit.com/deep-sleep-with-circuitpython/sleep-memory 
created wakeful.py to be used for future projects too. Thanks to James McKeown for helping me figure it out. 

Also shoutout to Adafruit Discord server saw bunch of examples on Deep Sleep 

Added the boot_out.txt as things change slightly between the version of CircuitPython

Adafruit CircuitPython 6.3.0 on 2021-06-01; Adafruit MagTag with ESP32S2

