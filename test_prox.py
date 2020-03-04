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

apds.setProximityIntLowThreshold(50)

print("Proximity Sensor Test")
print("=====================")
apds.enableProximitySensor()

oval = -1
while True:
    sleep(0.25)
    val = apds.readProximity()
    if val != oval:
        print("proximity={}".format(val))
        oval = val
