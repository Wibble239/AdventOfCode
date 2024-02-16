import re
score = 0
with open("input.txt") as f:
    for line in f:
        count = 0
        card = line.split(": ")[1]
        split = card.split("|")
        win = split[0].split(" ")
        win = [int(item) for item in win if item != ""]
        numbers = split[1].replace("\n", "").split(" ")
        numbers = [int(item) for item in numbers if item != ""]
        print("win =",win)
        print("Numbers =",numbers)
        for num in win:
            if num in numbers:
                count += 1
        if count > 0:
            score += 2 ** (count - 1)
        print(score)
