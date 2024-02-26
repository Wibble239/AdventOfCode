import re
with open("input.txt") as f:
    games = {}
    for line in f:
        count = 0
        game, card = line.split(": ")
        game = int(game.split(" ", 1)[1])
        split = card.split("|")
        win = split[0].split(" ")
        win = [int(item) for item in win if item != ""]
        numbers = split[1].replace("\n", "").split(" ")
        numbers = [int(item) for item in numbers if item != ""]
        for num in win:
            if num in numbers:
                count += 1
        if game not in games:
            games.update({game:0})
        games.update({game:(games.get(game)+1)}) 
        for x in range(games[game]):
            for i in range(1,count+1):
                if game+i in games:
                    games.update({game+i:(games.get(game+i)+1)})
                else:
                    games.update({game+i:1})
    total = sum(games.values())
    print(total)