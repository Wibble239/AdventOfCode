import numpy as np

with open("AdventOfCode/2024/Day1/input.txt") as f:
    data = f.readlines()

left = []
right = []

for line in data:
    left.append(int(line.split()[0].strip()))
    right.append(int(line.split()[1].strip()))

left.sort()
right.sort()

diff = abs(np.subtract(left, right))

total = sum(diff)

print(total)

SimScore = 0

for id in range(len(left)):
    SimScore += (right.count(left[id]) * left[id])

print(SimScore)