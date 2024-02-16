import re

total = 0

with open("input.txt") as f:
    for line in f:
        min = {"red": 0, "green": 0, "blue": 0}
        for x, colour in re.findall("(\d+) (red|green|blue)", line):
            if min[colour] < int(x):
                min[colour] = int(x)
        total += (min["red"] * min["green"] * min["blue"])

print(total)