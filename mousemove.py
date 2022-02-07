from adafruit_hid.mouse import Mouse
import board
import time
import digitalio
import usb_hid


mouse = Mouse(usb_hid.devices)

led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT
led.value = False
time.sleep(5)
while True:
  led.value = True
  mouse.move(x=2)
  led.value=False
  time.sleep(0.5)
  led.value=True
  mouse.move(x=-3)
  led.value=False
  time.sleep(0.5)
  
