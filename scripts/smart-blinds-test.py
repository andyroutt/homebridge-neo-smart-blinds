#!/usr/bin/env python
#
# Description: Neo Smart Blind Controller Test Script (HTTP)
# Author: Andy Routt
# License: MIT
# Version: 1.1
# Credits: Neo Controller Basic Open Local HTTP API Documentation
#

# Import Modules

import os
import sys
import requests
from tabulate import tabulate
from datetime import datetime

# Define Variables

controller = "[smart controller ip_address]"
id = "[smart controller id]"
id1 = "[room id1]"
id2 = "[room id2]"
dt = datetime.now()
hash = str(dt.microsecond * 10)

# Name Blinds

blind1 = "Window 1"
blind2 = "Window 2"
blind3 = "Window 3"
blind4 = "All Blinds"


# Specify Blinds to Control

def print_menu0():
    os.system('clear')
    print "Neo Smart Blind Controller Test Script (HTTP)"
    print ""
    print 20 * "-" , "Select Blind" , 20 * "-"
    print "1. " + blind1
    print "2. " + blind2
    print "3. " + blind3
    print "4. " + blind4
    print 53 * "-"
 
loop0=True
 
while loop0:
    print_menu0()
    blind = raw_input("Enter your choice: ")

    if blind=="1":
        name = blind1
        channel = "[controller channel for window 1]"
        break

    elif blind=="2":
        name = blind2
        channel = "[controller channel for window 2]"
        break

    elif blind=="3":
        name = blind3
        channel = "[controller channel for window 3]"
        break

    elif blind=="4":
        name = blind4
        channel = "15"
        break

    else:
        raw_input("Invalid Selection. Press Any Key to Continue.")

# Select Command

def print_menu1():
    os.system('clear')
    print "Neo Smart Blind Controller Test Script"
    print ""
    print 20 * "-" , "Command" , 20 * "-"
    print "0. Up"
    print "1. Down"
    print "2. Stop"
    print 53 * "-"

loop1=True
 
while loop1:
    print_menu1()
    action = raw_input("Enter your choice: ")

    if action=="0":
        action_name = "Raise"
        command = "up"
	break

    elif action=="1":
        action_name = "Lower"
        command = "dn"
        break

    elif action=="2":
        action_name = "Stop"
        command = "sp"
        break

    else:
        raw_input("Invalid Selection. Press Any Key to Continue.")

url = "http://" + controller + ":8838/neo/v1/transmit?command=" + id1 + "." + id2 + "-" + channel + "-" + command + "&id=" + id + "&hash=" + hash

answer = raw_input("Send Command to " + action_name + " " + name + "? (Y/N)? ")

# Submit Command

if answer=="y" or answer=="Y":
    response = requests.get(url)
    response_code = str(response.status_code)
else:
    response_code = "100"

# Print Summary

def print_summary():

    os.system('clear')
    print "Neo Smart Blind Controller Test Script"
    print ""
    print "GET Connection String:"
    print url
    print ""
    print tabulate([
        ['name', name],
        ['controller', controller],
        ['ID', id],
        ['ID1', id1],
        ['ID2', id2],
        ['hash', hash],
        ['channel', channel],
        ['command', command],
        ['action_name', action_name],        
        ['response_code', response_code]], headers=['Variable','Value'], tablefmt='grid')
    print ""

print_summary()

# Print Controller Response

if response_code == "100":
    print "Testing - Command Not Sent"
    print ""

elif response_code == "200":
    print "OK - Message received and transmitted by the Controller"
    print ""

elif response_code == "400":
    print "Bad Request - Command not found or not valid"
    print ""

elif response_code == "401":
    print "Unauthorized - Particle_ID not found or not valid"
    print ""

elif response_code == "404":
    print "Not Found - /neo/v1/transmit not found or not valid"
    print ""

elif response_code == "409":
    print "Conflict - hash # found, format is valid, but # was already used"
    print ""

else:
    print "Unknown Error"
    print ""



      