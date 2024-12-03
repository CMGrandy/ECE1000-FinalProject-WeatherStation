from machine import Pin, SoftI2C
import ssd1306
from time import sleep
import dht

led1_pin = 18
led2_pin = 19
led3_pin = 20
led4_pin = 21
sensor = dht.DHT11(Pin(22))
led1 = Pin(led1_pin, Pin.OUT)
led2 = Pin(led2_pin, Pin.OUT)
led3 = Pin(led3_pin, Pin.OUT)
led4 = Pin(led4_pin, Pin.OUT)
i2c = SoftI2C(scl=Pin(5), sda=Pin(4))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

while True:
  try:
    sleep(1)
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    temp_f = temp * (9/5) + 32.0
    if temp_f <= 32:
        led1.value(1)
        led2.value(0)
        led3.value(0)
        led4.value(0)
    elif temp_f <= 50:
        led1.value(1)
        led2.value(1)
        led3.value(0)
        led4.value(0)
    elif temp_f <= 75:
        led1.value(1)
        led2.value(1)
        led3.value(1)
        led4.value(0)
    elif temp_f <= 95:
        led1.value(1)
        led2.value(1)
        led3.value(1)
        led4.value(1)
    temp_string = str(temp)
    hum_string = str(hum)
    temp_f_string = str(temp_f)
    oled.text("WEATHER STATION" ,0 ,0)
    oled.text("DEG C:", 0, 30)
    oled.text("DEG F:", 0, 40)
    oled.text("HUM %", 0, 50)
    oled.text(temp_string, 45, 30)
    oled.text(temp_f_string, 45, 40)
    oled.text(hum_string, 45, 50)
    oled.show()
    sleep(10)
    oled.fill(0)
    oled.show()
  except OSError as e:
    oled.text('Failed to read sensor.')
    oled.show()
    

