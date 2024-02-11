import re
calibration = 0
nums = {"one": "1", 
        "two": "2", 
        "three": "3", 
        "four": "4", 
        "five": "5", 
        "six": "6", 
        "seven": "7", 
        "eight": "8", 
        "nine": "9"}
with open("input.txt") as f:
    for line in f:
        digits = []
        for x, c in enumerate(line):
            if line[x].isdigit():
                digits.append(line[x])
            else:
                for k in nums.keys():
                    if line[x:].startswith(k):
                        digits.append(nums[k])
        calibration += int(digits[0] + digits[-1])

print(calibration)
