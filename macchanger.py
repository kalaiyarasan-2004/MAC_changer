#!/usr/bin/env python

import subprocess

print("welcome to MAC changer")

interface=input("Enter the interface you want to change: ")
mac = input("Enter mac: ")

subprocess.call("ifconfig "+interface+" down",shell=True)
subprocess.call("ifconfig "+interface+" hw ether "+mac,shell = True)
subprocess.call("ifconfig "+interface+" up",shell=True)

print("The "+interface+" mac address changed to "+mac)
