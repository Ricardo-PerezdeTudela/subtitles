# Shifts every time instance of a typical subtitle file by an amount defined by the user. 
# Useful to synchronize with the video. 

#!/usr/bin/env python3
import argparse
from datetime import datetime, timedelta

parser = argparse.ArgumentParser()
parser.add_argument("--file", dest="filename", type=str, help="name of the subtitles file")
parser.add_argument("--dt", dest="dt", type=int, help="delay (in seconds)")
args = parser.parse_args()

arrow = "-->"
format = "%H:%M:%S,%f"

file = open(args.filename, "r") 

for line in file:
    if line.find(arrow) != -1:
        tt = line.rstrip('\n').split()
        tt.remove(arrow)
        t1 = datetime.strptime(tt[0],format) + timedelta(seconds=args.dt)
        t2 = datetime.strptime(tt[1],format) + timedelta(seconds=args.dt)
        t1 = t1.time().strftime(format)[:-3]
        t2 = t2.time().strftime(format)[:-3]
        print (t1,arrow,t2)
    else:
        print(line.rstrip('\n'))

