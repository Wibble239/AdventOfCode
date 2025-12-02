import re

with open("AdventOfCode/2025/Day02/input.txt") as f:
    data = f.read().split(",")

total = 0

for idrange in data:
    start, end = idrange.split("-")
    for i in range(int(start), int(end) + 1):
        if str(i)[:(len(str(i))//2)] == str(i)[(len(str(i))//2):]:
            total += i

print("part 1: ", total)

total2 = 0

for idrange in data:
    start, end = idrange.split("-")
    for i in range(int(start), int(end) + 1):
        if re.search(r"^(.+)\1+$", str(i)):
            total2 += i

print("part 2: ", total2)