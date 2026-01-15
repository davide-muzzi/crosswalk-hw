from machine import Pin
from utime import sleep

streetLight = {
    "red": Pin(6, Pin.OUT),
    "yellow": Pin(7, Pin.OUT),
    "green": Pin(8, Pin.OUT)
}
pedestrianLight = {
    "red": Pin(18, Pin.OUT),
    "yellow": Pin(19, Pin.OUT),
    "green": Pin(20, Pin.OUT)
}
pedestrian = False
car = True



print("LED starts flashing...")
while True:
    try:
        if car == True:
            pedestrianLight["red"].toggle()
            streetLight["green"].toggle()
        sleep(1) # sleep 1sec
    except KeyboardInterrupt:
        break
pedestrianLight["red"].off()
streetLight["green"].off()
print("Finished.")