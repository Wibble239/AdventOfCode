with open("AdventOfCode/2025/Day01/input.txt") as f:
    data = f.read().splitlines()

position = 50
count = 0

for turn in data:
    direction, step = turn[0], int(turn[1:])
    match direction:
        case 'L':
            position -= step
        case 'R':
            position += step
    position %= 100
    if position == 0:
        count += 1

print("Part 1: ", count)

position2 = 50
count2 = 0

for turn in data:
    direction, step = turn[0], int(turn[1:])
    match direction:
        case 'L':
            for i in range(step):
                position2 -= 1
                position2 %= 100
                if position2 == 0:
                    count2 += 1
        case 'R':
            for i in range(step):
                position2 += 1
                position2 %= 100
                if position2 == 0:
                    count2 += 1

print("Part 2: ", count2)