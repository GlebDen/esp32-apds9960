from time import sleep
import machine
from machine import Pin, I2C
from const import *
from device import uAPDS9960 as APDS9960

sda_pin = machine.Pin(21)
scl_pin = machine.Pin(22)
rst_pin = machine.Pin(19) #not sure it used

bus = machine.I2C(sda=sda_pin, scl=scl_pin)
apds = APDS9960(bus)

dirs = {
    APDS9960_DIR_NONE: "none",
    APDS9960_DIR_LEFT: "left",
    APDS9960_DIR_RIGHT: "right",
    APDS9960_DIR_UP: "up",
    APDS9960_DIR_DOWN: "down",
    APDS9960_DIR_NEAR: "near",
    APDS9960_DIR_FAR: "far",
}

apds.setProximityIntLowThreshold(50)

print("Gesture Test")
print("============")
apds.enableGestureSensor()

while True:
    sleep(0.5)
    if apds.isGestureAvailable():
        motion = apds.readGesture()
        print("Gesture={}".format(dirs.get(motion, "unknown")))
