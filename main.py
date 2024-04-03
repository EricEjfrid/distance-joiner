import json
import sys
from datetime import datetime, timedelta 

source_path = sys.argv[1]

target_path = list()

for element in sys.argv:
    if (element == target_path):
        continue
    target_path.append(element)

f = open(source_path)

source_lines = f.readlines()

f.close()

target_files = list()

for element in target_path:
    f=open(element)
    target_lines = f.readlines()
    f.close()
    target_files.append(target_lines)


def transplant_distance(source_lines, target_files):
    distance_lines = list()

    # Find distance lines in the source file
    for line in source_lines:
        if("- D -" in line):
            distance_lines.append(line)

    #Add distance lines to the target data
    for file in target_files:
        file.append(distance_lines)
        file.sort(key=lambda x: x.split()[0])

    # Sort target data 

    return target_files

outputdata = transplant_distance(source_lines, target_files)

#test comment
for element in outputdata:
    with open(argv[2] + "-distance.txt","W") as file:
        for line in element:
            file.write(f"{line}")
