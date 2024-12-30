def searchboard(board, row, col, word):

    count = 0
    m = len(board)
    n = len(board[0])

    if board[row][col] != word[0]:
        return False
    
    wordlength = len(word)

    # Setting the 8 directions, starting top left
    x = [-1, 0, 1, -1, 1, -1, 0, 1]
    y = [-1, -1, -1, 0, 0, 1, 1, 1]

    for direction in range(8):

        currentx = row + x[direction]
        currenty = col + y[direction]
        k = 1

        while k < wordlength:

            if currentx >= m or currentx < 0 or currenty >= n or currenty < 0:
                break

            if board[currentx][currenty] != word[k]:
                break

            currentx += x[direction]
            currenty += y[direction]
            k += 1

        if k == wordlength:
            count += 1

    return count

def searchword(board, word):

    answer = 0

    for i in range(len(board)):
        for j in range(len(board[0])):
            answer += searchboard(board, i, j, word)

    return answer

with open("AdventOfCode/2024/Day04/input.txt") as f:
    data = f.read().strip()

word = "XMAS"
board = [list(i) for i in data.split("\n")]

total = searchword(board, word)

print("Part 1:", total)