#!/usr/bin/env python

import subprocess

print("welcome to MAC changer")

mac = input("Enter mac: ")

subprocess.call("ifconfig eth0 down",shell=True)
subprocess.call("ifconfig eth0 hw ether "+mac,shell = True)
subprocess.call("ifconfig eth0 up",shell=True)

print("The mac changed to "+mac)
