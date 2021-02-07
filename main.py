import subprocess
import csv
from datetime import datetime
from time import sleep

cmd = ['cat', '/proc/net/wireless']
proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

o, e = proc.communicate()

def find(num, string):
    return str(o)[num + (str(o).find(string))]

with open('graph.csv', mode='w') as f:
    writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    writer.writerow(["Link Quality", "Signal Level", "Time Stamp"])

    while True:
        date = datetime.now()

        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        o, e = proc.communicate()

        link_quality = (find(14, "wlan0") + find(15, "wlan0")) # out of 100, higher is better 
        signal_level = 100 - int(find(20, "wlan0") + find(21, "wlan0")) # between 30 and 90, measured in -dBm, lower is better. 

        writer.writerow([link_quality, signal_level, date.second])
        print(link_quality, signal_level)

        sleep(5)





