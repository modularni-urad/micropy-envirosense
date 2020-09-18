# micropy-envirosense

PyBoard ($9, running [micropython](http://micropython.org/)) based device sensing basic environmental data:
- teperature, humidity: https://gitlab.com/georgedorn/tinysnakes/blob/master/client/htu21d.py, https://forum.micropython.org/viewtopic.php?t=647
- PMx particles: https://github.com/pkucmus/micropython-pms7003/
- noise
- TODO..

#### LoRa connection
Nekolik ks osazenych https://www.tindie.com/products/DrAzzy/rn2483-breakout-bare-board/
Nebo alternativa (doexperimentovat): LoRa modul SX1276 + WAN implementace jako knihovna v MCU.

![overview](./pics/overview.jpg)
![detail](./pics/detail.jpg)

## how to start

```
sudo apt install picocom
picocom /dev/ttyACM0
```
… primo do micro python
… pak pro exit: Ctrl + A + X

Nebo primo:
```
wget https://raw.githubusercontent.com/micropython/micropython/master/tools/pyboard.py
python pyboard.py
python ~/pyboard.py /media/vencax/4621-0000/boot.py
```

LORA links:
https://lemariva.com/blog/2018/10/micropython-esp32-sending-data-using-lora
https://www.google.com/search?q=SX1276+micropython
https://forum.micropython.org/viewtopic.php?t=4144
https://github.com/aizukanne/ESP32-micropython-lora
https://github.com/mallagant/uLoRaWAN
https://medium.com/gowombat/iot-lora-with-micropython-on-the-esp8266-and-esp32-59d1a4b507ca

Brainstorm dokumenty:
https://docs.google.com/document/d/1pF_UjhEmnwvRKELV9iwkjFdgDIjeJpardr_JQ9LFgzI/edit
https://docs.google.com/document/d/1ZG-MrM6UnbTOYpQVG2sRkgkO5HKnYeKKxtdgV-Pe9vE/edit
