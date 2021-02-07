import subprocess
import csv
from datetime import datetime
from time import sleep
import speedtest

cmd = ['cat', '/proc/net/wireless']
proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
o, e = proc.communicate()

st = speedtest.Speedtest()


def find(num, string):
    return str(o)[num + (str(o).find(string))]

with open('wifi.csv', mode='w') as f:
    writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["Link Quality", "Signal Level", "Time Stamp"])

    for i in range(1, 50):
        date = datetime.now()

        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        o, e = proc.communicate()

        link_quality = (find(14, "wlan0") + find(15, "wlan0")) # out of 100, higher is better 
        signal_level = 100 - int(find(20, "wlan0") + find(21, "wlan0")) # between 30 and 90, measured in -dBm, lower is better. 

        writer.writerow([link_quality, signal_level, date.second])
        print(link_quality, signal_level)

        

        sleep(5)

with open('internet.csv', mode='w') as f:
    writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["Upload", "Download", "Time Stamp"])

    for i in range(1, 20):
        date = datetime.now()

        writer.writerow(st.upload() / 100000, st.download() / 100000, date.second())
