import re
calibration = 0
with open("input.txt") as f:
    for line in f:
        code = re.sub("[^0-9]","",line)
        digits = int(code[0] + code[-1])
        calibration += digits

print(calibration)
