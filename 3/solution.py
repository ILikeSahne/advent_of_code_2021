import os
import sys

def calcPowerCon():
    file_path = os.path.join(sys.path[0], "input.txt")
    input = open(file_path, 'r')
    lines = input.readlines()
    size = len(lines[0])
    numbers = [0] * (size - 1)
    for line in lines:
        for i, c in enumerate(line):
            if c == '1':
                numbers[i] += 1

    # numbers = numbers[::-1]

    sum1 = 0
    sum2 = 0
    for i, x in enumerate(numbers):
        sum1 = sum1 << 1
        sum2 = sum2 << 1
        if x > len(lines) - x:
            sum1 += 1
        else:
            sum2 += 1
    return sum1 * sum2

print("Power is:", calcPowerCon())