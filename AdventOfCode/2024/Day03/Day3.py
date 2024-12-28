import re

with open("AdventOfCode/2024/Day03/input.txt") as f:
    data = f.read()

clean = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)", data)

total = 0
for mul in clean:
    x = re.findall("[0-9]{1,3}", mul)
    total += int(x[0]) * int(x[1])

print("Part 1:", total)

clean2 = re.findall("do\(\)|don\'t\(\)|mul\([0-9]{1,3},[0-9]{1,3}\)", data)

total2 = 0
do = True
for mul in clean2:
    if mul == "do()":
        do = True
    elif mul == "don't()":
        do = False
    else:
        if do:
            x = re.findall("[0-9]{1,3}", mul)
            total2 += int(x[0]) * int(x[1])

print("Part 2:", total2)