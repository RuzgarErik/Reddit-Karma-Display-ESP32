import machine, ssd1306
import network
import time
import urequests as requests
import json
sta_if = network.WLAN(network.STA_IF)
ap_if = network.WLAN(network.AP_IF)
sta_if.active(True)
sta_if.connect('<wifiapname>', '<wifipass>')
for i in range(50):
  if sta_if.isconnected():
    break
  time.sleep_ms(100)
else:
  raise RuntimeError('WiFi connection failed')
i2c = machine.I2C(scl=machine.Pin(4), sda=machine.Pin(5))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
oled.fill(0)
while(1):
    time.sleep(1)
    r = requests.get('https://www.reddit.com/user/ruzgarerik/about.json')
    data = r.json()
    karma = data['data']['link_karma'] + data['data']['comment_karma']
    oled.fill(0)
    for i in range(1,128):
        oled.pixel(i+1,0,1)
    oled.text("Reddit Karma",18,5,1)
    for i in range(1,128):
        oled.pixel(i+1,15,1)
    for i in range(1,64):
        oled.pixel(0,i+1,1)
    for i in range(1,64):
        oled.pixel(127,i+1,1)
    oled.text(str(karma),39,25,1)
    for i in range(1,128):
        oled.pixel(i+1,40,1)
    oled.text("u/ruzgarerik",13,50,1)
    for i in range(1,128):
        oled.pixel(i+1,63,1)
    oled.show()
