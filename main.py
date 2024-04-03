import json
import sys
from datetime import datetime, timedelta 

source_path = sys.argv[1]
target_path = sys.argv[2]

f = open(source_path)

source_lines = f.readlines()

f.close()

f = open(target_path)

target_lines = f.readlines()

f.close()

def transplant_distance(source_lines, target_lines):
    distance_lines = list()

    for line in source_lines:
        if("- D -" in line):
            distance_lines.append(line)

    target_lines.append(distance_lines)

    target_lines.sort(key=lambda x: x.split()[0])

    return target_lines

outputdata = transplant_distance(source_lines, target_lines)

with open("distance-added.txt","W") as file:
    for line in outputdata:
        file.write(f"{line}")
