#!/usr/bin/python

import time
import datetime
from Adafruit_16x8 import SixteenByEight

# ===========================================================================
# 16x8 Pixel Example
# ===========================================================================
grid = SixteenByEight(address=0x70)

print "Press CTRL+Z to exit"

# Continually update the 16x8 display one pixel at a time
while(True):
  for x in range(0, 8):
    for y in range(0, 16):
      grid.setPixel(x, y)
      time.sleep(0.05)
  time.sleep(0.5)
  grid.clear()
  time.sleep(0.5)
