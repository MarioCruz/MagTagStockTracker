import time
import terminalio
import neopixel
import alarm
import board
import json
import math
from adafruit_magtag.magtag import MagTag
from analogio import AnalogIn
from wakeful import store_data, load_data

#NeoPix Colors
RED = 0x880000
GREEN = 0x008800
BLUE = 0x000088
YELLOW = 0x884400
CYAN = 0x0088BB
MAGENTA = 0x9900BB
WHITE = 0x888888

SYNCHRONIZE_CLOCK = True

#Prepare Stock Api
STOCK1 = "WSO"
# Set up where we'll be fetching data from
# Get a free API/token from here https://finnhub.io/
DATA_SOURCE = (
    "https://finnhub.io/api/v1/quote?symbol=" + STOCK1 + "&token="
)
#Parse the Json data
DATA1_LOCATION = ["c"]  #  Current price
DATA2_LOCATION = ["h"]  #  High price of the day
DATA3_LOCATION = ["l"]  #  Low price of the day
DATA4_LOCATION = ["pc"]  #  Prevoius Close

#Set the pin for Battery
analog_in = AnalogIn(board.A1)

#----------------Functions--------------------

def get_voltage(pin):
    return (pin.value * 3.3) / 65536

def blink(color, duration):
    magtag.peripherals.neopixel_disable = False
    magtag.peripherals.neopixels.fill(color)
    time.sleep(duration)
    magtag.peripherals.neopixel_disable = True

def text_Current(val):
    return "$%g " % val + STOCK1

def text_High(val):
    return "$%g High" % val

def text_Low(val):
    return "$%g Low" % val

def text_Close(val):
    return "$%g PrvClose" % val

#Main
#Set Data
magtag = MagTag(
    url=DATA_SOURCE,
    json_path=(DATA1_LOCATION, DATA2_LOCATION, DATA3_LOCATION, DATA4_LOCATION),
)

#Get Time
magtag.network.connect()
magtag.network.get_local_time()

#Get Background
magtag.graphics.set_background("/bmps/magtag_quotes_bg.bmp")

#Get batery info
voltage = magtag.peripherals.battery

#Print to the eInk
#  Current Stock quote in bold text
magtag.add_text(
    text_transform=text_Current,
    text_font="/fonts/LeagueGothic-Regular-36.pcf",
    text_position=(
        (magtag.graphics.display.width // 2) - 1,
        31,
    ),
    text_anchor_point=(0.5, 0.7),
)

# High Quote in italic text, no wrapping
magtag.add_text(
    text_transform=text_High,
    text_font="/fonts/Arial-Bold-12.pcf",
    text_position=(
        (magtag.graphics.display.width // 2) - 1,
        60,
    ),
    text_anchor_point=(0.5, 0.4),
)
# Low Quote in italic text, no wrapping
magtag.add_text(
    text_transform=text_Low,
    text_font="/fonts/Arial-Italic-12.pcf",
    text_position=(
        (magtag.graphics.display.width // 2) - 1,
        80,
    ),
    text_anchor_point=(0.5, 0.3),
)
# Prevoius Quote in italic text, no wrapping
magtag.add_text(
    text_transform=text_Close,
    text_font="/fonts/Arial-Bold-12.pcf",
    text_position=(
        (magtag.graphics.display.width // 2) - 1,
        120,
    ),
    text_anchor_point=(0.5, 0.75),
)

#Go Get the Info
print("Fetchiing Data from JSON")

try:
    value = magtag.fetch()
    print("Response is", value)
    TS = time.localtime()
    print(TS)
except (ValueError, RuntimeError) as e:
    print("Some error occured, retrying! -", e)
    magtag.refresh()

CurrentPrice = float(value[0])
print(CurrentPrice)
PrvPrice=load_data()
print(PrvPrice)


if CurrentPrice >= PrvPrice:
    blink(GREEN, .8)
else:
    blink(RED, .8)

store_data(CurrentPrice)


#alarm.sleep_memory[0] = PrvPrice

print(voltage)
if voltage < 1.9:
    magtag.peripherals.play_tone(165, 1)

#Undecided on the sound I want to make when the batery is low
#                            (Freq,Length)
#magtag.peripherals.play_tone(9980, 0.15)
#magtag.peripherals.play_tone(880, 0.15)
#magtag.peripherals.play_tone(147, 1)
#magtag.peripherals.play_tone(175, 1)
#magtag.peripherals.play_tone(196, 1)
#magtag.peripherals.play_tone(131, 1)

CurrentTime = (TS[3])
print(CurrentTime)
print(TS)

# Create a an alarm that will trigger x seconds from now.
time_alarm = alarm.time.TimeAlarm(monotonic_time=time.monotonic() +30)

#Future Use even more deep sleep based on clock time for 6pm to 6am
#if CurrentTime > 6:
#    alarm.exit_and_deep_sleep_until_alarms(time_alarm)
#else:
#    magtag.exit_and_deep_sleep(900)

#Deep sleep for 290 seconds to save the battery
magtag.exit_and_deep_sleep(290) 
