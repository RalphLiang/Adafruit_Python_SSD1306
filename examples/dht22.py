import time
import board
import adafruit_dht

dht_device = adafruit_dht.DHT22(board.D4)

temperature = dht_device.temperature
humidity = dht_device.humidity

if humidity is not None and temperature is not None:
    print("Temp={0:0.2f}*C  Humidity={1:0.2f}%".format(temperature, humidity))
else:
    print("Failed to retrieve data from HDT22 sensor")

time.sleep(5)
