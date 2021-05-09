# branch A2

from fpioa_manager import fm
from Maix import GPIO

# 13 - green  12 - blue  14 - red
io_red = 13
fm.register(io_red, fm.fpioa.GPIO0)

led_r=GPIO(GPIO.GPIO0, GPIO.OUT)
led_r.value(0)

