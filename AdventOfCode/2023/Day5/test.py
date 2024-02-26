import re

with open("input.txt") as f:
    puzzle_input = f.read()

def convert(input, conversion):
    changes = re.findall(r'(\d+) (\d+) (\d+)', conversion)
    for change in changes:
        dest, start, delta = map(int, change)
        if start <= input < start + delta:
            return input + dest - start
    return input

low = []

Seeds, Conv = puzzle_input.split("\n\n", 1)
Conv = Conv.split("\n\n")
Seeds = list(map(int, re.findall(r'\d+', Seeds)))
for x in range(len(Seeds)):
    if x % 2 != 0:
        NewSeeds = [y for y in range(Seeds[x-1], (Seeds[x-1] + Seeds[x]))]
        locations = [convert(seed, Con) for seed in NewSeeds for Con in Conv]
        low.append(min(locations))
print(min(low))
