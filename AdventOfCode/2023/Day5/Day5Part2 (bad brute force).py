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

low = []

Seeds, Conv = puzzle_input.split("\n\n", 1)
Conv = Conv.split("\n\n")
Seeds = list(map(int, re.findall(r'\d+', Seeds)))
for x in range(len(Seeds)):
    if x % 2 == 0:
        NewSeeds = []
        first = Seeds[x]
    else:
        NewSeeds = [y for y in range(Seeds[x-1], (Seeds[x-1] + Seeds[x]))]
        print(len(NewSeeds))
        test = set(NewSeeds)
        print(len(test))
        locations = []
        for seed in NewSeeds:
            val = seed
            for Con in Conv:
                val = convert(val, Con)
            locations.append(val)
        low.append(min(locations))
print(min(low))