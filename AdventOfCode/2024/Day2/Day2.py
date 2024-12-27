def safe_check(x):
    if x == sorted(x) or x == sorted(x, reverse = True):
        for i in range(len(x) - 1):
            if not 0 < abs(x[i] - x[i + 1]) < 4:
                return False        
        return True

with open("AdventOfCode/2024/Day2/input.txt") as f:
    data = f.readlines()

count = 0
for line in data:
    n = [int(num.strip()) for num in line.split()]
    if safe_check(n):
        count += 1

print("Part 1:",count)

count2 = 0
for line in data:
    nums = [int(num.strip()) for num in line.split()]
    if safe_check(nums):
        count2 += 1
    else:
        for i in range(len(nums)):
            temp = nums.copy()
            temp.pop(i)
            if safe_check(temp):
                count2 += 1
                break

print("Part 2:", count2)