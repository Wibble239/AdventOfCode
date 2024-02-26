import re

with open("input.txt") as f:
    puzzle_input = f.read()

def convert(input, conversion):
    changes = re.findall(r'(\d+) (\d+) (\d+)', conversion)
    for change in changes:
        dest, start, delta = map(int, change)
        if input in range(start, start + delta):
            output = input + dest - start
            break
        else:
            output = input
    return output

locations = []
Seeds, Conv = puzzle_input.split("\n\n", 1)
Conv = Conv.split("\n\n")
Seeds = re.findall(r'\d+', Seeds)

for seed in Seeds:
    val = seed
    for Con in Conv:
        val = convert(int(val), Con)
    locations.append(val)
print(min(locations))