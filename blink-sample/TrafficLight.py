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


def redLight(light):
    light["green"].off()
    light["yellow"].on()
    sleep(2)
    light["yellow"].off()
    light["red"].on()


print("LED starts flashing...")
while True:
    try:
        if car == True:
            pedestrianLight["red"].on()
            pedestrianLight["yellow"].off()
            pedestrianLight["green"].off()
            streetLight["red"].off()
            streetLight["yellow"].off()
            streetLight["green"].on()
        sleep(1) # sleep 1sec
    except KeyboardInterrupt:
        break
pedestrianLight["red"].off()
streetLight["green"].off()
print("Finished.")
