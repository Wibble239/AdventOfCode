with open("AdventOfCode/2025/Day03/input.txt") as f:
    data = f.read().splitlines()

joltage = 0

for bank in data:
    for i in range(9, 0, -1):
        if bank[:len(bank)-1].find(str(i)) != -1:
            start = i
            pos = bank[:len(bank)-1].find(str(i))
            break
    for i in range(9, 0, -1):
        if bank[pos+1:].find(str(i)) != -1:
            end = i
            break
    joltage += int(str(start)+str(end))


print("Part 1:", joltage)