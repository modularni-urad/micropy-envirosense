# import machine
from pyb import Pin, ADC, Timer, UART, LED
from pyb import I2C
from client_htu21d import HTU21D
from pms7003_passive import PassivePMS7003, IncorrectData

import micropython
micropython.alloc_emergency_exception_buf(100)

workLed = LED(2)    # 1=red, 2=green, 3=yellow, 4=blue
noiseLed = LED(1)
pinNoiseThreshold = Pin('X2', Pin.IN, Pin.PULL_UP)
noiseLevelADC = ADC(Pin('X11'))
# siranLevelADC = ADC(Pin('X12'))
tempDriver = HTU21D(I2C(2, I2C.MASTER))
dustDriver = PassivePMS7003(UART(4))    # X1 - tx, X2 - r

# ---------------------------

temperature = 0
humidity = 0

def do_work(_):
    workLed.on()
    temperature = tempDriver.readTemperatureData()
    humidity = tempDriver.readHumidityData()
    print(temperature)
    print(humidity)
    dustDriver.wakeup()
    try:
        rr = dustDriver.read()
        print(str(rr))
    except IncorrectData:
        print('bad data')
    finally:
        dustDriver.sleep()
    workLed.off()

freq = 1 / 8  # once per 100s
tim = Timer(1, freq=freq)
tim.callback(lambda _: micropython.schedule(do_work, 0))

# ---------  SOUND  ------------------------------------------------------------
avgSound = 0
n = 1
overNoisedCount = 0
noiseLevel = 0

def senseNoise(t):
  global n, noiseLevel, overNoisedCount
  noiseLed.toggle()
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
