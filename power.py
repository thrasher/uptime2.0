#!/usr/bin/python
#
# Control power-hungry pi parts
#
# Note: some of these don't reset after a reboot, so be careful what you shut off!
#

import os
import time

# handle one-line on/off commands
def manage(name, isOn, onCmd, offCmd):
	cmd = ""
	if (isOn):
		# turn on
		cmd = onCmd
	else:
		# turn off
		cmd = offCmd

	stream = os.popen(cmd)
	output = stream.read().lstrip().rstrip()
	print(name + " change state: " + output)

def wifi(isOn):
	# sudo rfkill list all
	manage("WiFi", isOn, "sudo rfkill unblock wifi", "sudo rfkill block wifi")
	# manage("WiFi", isOn, "sudo iwconfig wlan0 txpower on", "sudo iwconfig wlan0 txpower off")

def bluetooth(isOn):
	manage("Bluetooth", isOn, "sudo rfkill unblock bluetooth", "sudo rfkill block bluetooth")

def hdmi(isOn):
	manage("HDMI", isOn, "tvservice --preferred", "tvservice --off")
	#manage("HDMI", isOn, "vcgencmd display_power 1", "vcgencmd display_power 0")

def usb(isOn):
	manage("USB/LAN IC", isOn, "echo '1-1' | sudo tee /sys/bus/usb/drivers/usb/bind", "echo '1-1' | sudo tee /sys/bus/usb/drivers/usb/unbind")

def pwrLed(isOn):
	manage("Power LED", isOn, "echo 255 | sudo tee /sys/class/leds/led1/brightness", "echo 0 | sudo tee /sys/class/leds/led1/brightness")

def actLed(isOn):
	manage("Activity LED", isOn, "echo 255 | sudo tee /sys/class/leds/led0/brightness", "echo 0 | sudo tee /sys/class/leds/led0/brightness")

# set all known devices to on/off power state
def power(isOn):
	wifi(isOn)
	bluetooth(isOn)
	pwrLed(isOn)
	actLed(isOn)
	time.sleep(10)
	usb(isOn)
	time.sleep(10)
	hdmi(isOn)

# turn everything on
def highPower():
	power(True)

# turn everything off
def lowPower():
	power(False)

print("shutting off peripherals")
wifi(False)
time.sleep(10)
print("turning on peripherals")
wifi(True)

