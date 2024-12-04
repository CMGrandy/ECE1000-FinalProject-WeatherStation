from machine import Pin, SoftI2C
import ssd1306
import time 
import dht
cur_time = time.localtime()

filename = str(cur_time[0]) + "_" +str(cur_time[1]) + "_" + str(cur_time[2]) + "_" + str(abs(cur_time[3]-12)) + "_" + str(cur_time[4]) + "_" + str(cur_time[5])
filename = "Weather_Station" + filename + ".txt"
file = open(filename,"w")

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

def saveData(tempC, tempF, Hum):
    cur_time = time.localtime()
    raw_time = (int(cur_time[3]) * 3600 ) + (int(cur_time[4]) * 60) + int(cur_time[5])
    file.write(str(raw_time) + " ")
    file.write("Temp C: "+ str(tempC))
    file.write(" Temp F: " + str(tempF))
    file.write(" Humidity(%): " + str(Hum))
    file.write("\n")





while True:
  try:
    
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
    oled.fill(0)
    oled.show()
    oled.text("WEATHER STATION" ,0 ,0)
    oled.text("DEG C:", 0, 30)
    oled.text("DEG F:", 0, 40)
    oled.text("HUM %", 0, 50)
    oled.text(temp_string, 45, 30)
    oled.text(temp_f_string, 45, 40)
    oled.text(hum_string, 45, 50)
    oled.show()
    saveData(temp, temp_f, hum)
    time.sleep(10)

  except OSError as e:
    oled.text('Failed to read sensor.')
    oled.show()


