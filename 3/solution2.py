import os
import sys

def calcPowerCon():
    file_path = os.path.join(sys.path[0], "input.txt")
    input = open(file_path, 'r')
    orig_lines = input.readlines()
    lines = orig_lines.copy()
    i = 0
    oxygen = ""
    while True:
        if len(lines) == 1:
            oxygen = lines[0]
            break
        mostCommon = mostCommonBit(lines, i)
        for l in lines[::-1]:
            if l[i] != mostCommon:
                lines.remove(l)
        i += 1

    lines = orig_lines.copy()
    i = 0
    CO2 = ""
    while True:
        if len(lines) == 1:
            CO2 = lines[0]
            break
        mostCommon = mostCommonBit(lines, i)
        for l in lines[::-1]:
            if l[i] == mostCommon:
                lines.remove(l)
        i += 1

    sum1 = 0
    sum2 = 0
    for i in range(len(oxygen) - 1):
        sum1 = sum1 << 1
        sum2 = sum2 << 1
        if oxygen[i] == '1':
            sum1 += 1
        if CO2[i] == '1':
            sum2 += 1
    return sum1 * sum2

    return CO2


def mostCommonBit(lines, pos):
    num0 = 0
    num1 = 0
    for l in lines:
        if l[pos] == '0':
            num0 += 1
        else:
            num1 += 1

    if num1 >= num0:
        return '1'
    return '0'

print("Power is:", calcPowerCon())