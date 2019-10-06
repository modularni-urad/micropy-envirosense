# import machine
from pyb import Pin, ADC, Timer, UART
from machine import I2C

import micropython
micropython.alloc_emergency_exception_buf(100)

pinNoiseThreshold = Pin('X2', Pin.IN, Pin.PULL_UP)
noiseLevelADC = ADC(Pin('X11'))
# siranLevelADC = ADC(Pin('X12'))
# tempI2C = I2C('X', freq=400000)
# PMxUART = UART(4, 9600) # X1 - tx, X2 - rx
#
# def sensePMx():
#   dustLevel = PMxUART.read(5)
#
# def senseTemp():
#   i2c.scan()                          # returns list of slave addresses
#   i2c.readfrom(0x42, 5)

def cback(t):
  global overNoisedCount
  print(overNoisedCount)

# ---------------------------

freq = 1 / 5  # once per 100s
tim = Timer(1, freq=freq)
tim.callback(cback)


# ---------  SOUND  ------------------------------------------------------------

avgSound = 0
n = 1
overNoisedCount = 0
noiseLevel = 0

def senseNoise(t):
  global n, noiseLevel, overNoisedCount
  val = pinNoiseThreshold.value()
  if val == 0:      # 0 = overnoise
    overNoisedCount += 1
  # noiseLevel = noiseLevelADC.read() # read value, 0-4095
  # vypocet prumeru: https://robotika.cz/guide/filtering/en
  # avgSound = avgSound + 1/n * (noiseLevel - avgSound)
  n += 1

# freq = 0.1  # once per 10s
noiseTimer = Timer(2, freq=1)
noiseTimer.callback(senseNoise)
# ------------------------------------------------------------------------------
