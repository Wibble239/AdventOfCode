import re

possible = {"red": 12, "green": 13, "blue": 14}
total = 0
game = 0
with open("input.txt") as f:
    for line in f:
        game += 1
        for x, colour in re.findall("(\d+) (red|green|blue)", line):
            if possible[colour] < int(x):
                break
        else:
            total += game

print(total)