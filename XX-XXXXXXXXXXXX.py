#!/usr/bin/env python
import os, glob, time, sys, datetime, requests
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

device_folder = glob.glob('/sys/bus/w1/devices/XXXXXXXXXXXXX*')
device_file = [device_folder[0] + '/w1_slave']

def read_temp_raw():
    f_1 = open(device_file[0], 'r')
    lines_1 = f_1.readlines()
    f_1.close()
    return lines_1

def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES' or lines[2].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t='), lines[3].find('t=')
    temp = float(lines[1][equals_pos[0]+2:])/1000
    return temp

temp = read_temp_raw()
outputmain= temp[1][-6:-4]
finaloutput= outputmain
print finaloutput

event = (finaloutput)
apikey = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

url = "https://maker.ifttt.com/trigger/%s/with/key/%s" % (event, apikey)
headers = {}
res = requests.post(url, headers=headers)

print "sent"
