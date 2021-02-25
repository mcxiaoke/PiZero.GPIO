#!/usr/bin/env python
"""Basic blinking led example.

The led on Pi Zero-OLinuXino-MICRO  blinks with rate of 1Hz like "heartbeat".
"""

import os
import sys

if not os.getegid() == 0:
    sys.exit('Script must be run as root')


from time import sleep
from pizero.gpio import gpio
from pizero.gpio import port
#//BY CHOW
from pizero.gpio import connector

__author__ = "Stefan Mavrodiev"
__copyright__ = "Copyright 2014, Olimex LTD"
__credits__ = ["Stefan Mavrodiev"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = __author__
__email__ = "support@olimex.com"


# 
"""
*/  {"LED",
        {
            {   "POWER_LED",  SUNXI_GPL(10),  1   },
            {   "STATUS_LED",  SUNXI_GPA(15),  2   },
"""
#led = connector.LEDp1    # This is the same as port.POWER_LED
#led = connector.LEDp2    # This is the same as port.STATUS_LED
led = connector.gpio1p10
#led = port.POWER_LED
#led = port.STATUS_LED

gpio.init()

for k in dir(connector):
    if k.startswith('gpio'):
        gpio.setcfg(getattr(connector,k), gpio.OUTPUT)
        
# gpio.setcfg(connector.gpio1p10, gpio.OUTPUT)
# gpio.setcfg(connector.gpio1p11, gpio.OUTPUT)
# gpio.setcfg(connector.gpio1p12, gpio.OUTPUT)
# gpio.setcfg(connector.gpio1p13, gpio.OUTPUT)
# gpio.setcfg(connector.gpio1p15, gpio.OUTPUT)
# gpio.setcfg(connector.gpio1p16, gpio.OUTPUT)
# gpio.setcfg(connector.gpio1p18, gpio.OUTPUT)
# gpio.setcfg(connector.gpio1p19, gpio.OUTPUT)
# 
# gpio.setcfg(connector.gpio1p21, gpio.OUTPUT)
# gpio.setcfg(connector.gpio1p22, gpio.OUTPUT)
# gpio.setcfg(connector.gpio1p23, gpio.OUTPUT)
# gpio.setcfg(connector.gpio1p24, gpio.OUTPUT)
# gpio.setcfg(connector.gpio1p26, gpio.OUTPUT)
# 
# gpio.setcfg(connector.gpio1p3, gpio.OUTPUT)
# gpio.setcfg(connector.gpio1p5, gpio.OUTPUT)
# gpio.setcfg(connector.gpio1p7, gpio.OUTPUT)
# gpio.setcfg(connector.gpio1p8, gpio.OUTPUT)

try:
    print ("Press CTRL+C to exit")
    while True:
#         gpio.output(connector.gpio1p10, 1)
        for k in dir(connector):
            if k.startswith('gpio'):
                gpio.output(getattr(connector,k), 1)
        print("gpio all set 1")
        sleep(1)
#         gpio.output(connector.gpio1p10, 0)
        for k in dir(connector):
            if k.startswith('gpio'):
                gpio.output(getattr(connector,k), 0)
        print("gpio all set 0")
        sleep(1)
        """
        gpio.output(led, 1)
        sleep(0.1)
        gpio.output(led, 0)
        sleep(0.1)

        sleep(0.6)
        """
except KeyboardInterrupt:
    print ("Goodbye.")

