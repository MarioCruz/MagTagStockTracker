#force Time update on MagTag

from adafruit_magtag.magtag import MagTag
import time
import rtc

magtag = MagTag()
magtag.network.get_local_time()
now = rtc.RTC().datetime

print(now)
