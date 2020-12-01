import math
import os
import random
import re
import sys

def btw2and10e6(steps):
    if steps >= 2 and steps <= 1000000:
        return True
    return False

def valid_path(path):
    if set(path).issubset({'U','D'}):
        return True
    return False




def step_value(step):
    if step == 'U':
        return 1
    else:
        return -1

def can_be_valley(levels, idx):
    if levels[idx] == 0 and levels[idx + 1] == -1 and idx + 1 < len(levels):
        return True
    return False

def is_valley(levels, idx):
    count = idx + 1
    while count < len(levels):
        if levels[count] == 0:
            return  True
        count += 1
    return False

def list_of_levels(path):
    idx = 0
    levels = [0]

    for step in list(path):
        if idx == 0:
            #levels.append(0)
            levels.append(step_value(step))

        elif idx < len(path):
            levels.append(levels[idx] + step_value(step))
        idx += 1
    return levels


def countingValleys(steps, path):
    levels = list_of_levels(path)
    idx = 0
    valleys = 0
    for idx in range(len(levels)):
        if can_be_valley(levels,idx):
            if is_valley(levels, idx):
                valleys += 1
    return valleys

if __name__ == '__main__':

    # path = 'UDDDDDD'
    # levels = list_of_levels(path)
    steps = int(input().strip())
    path = input()

    if btw2and10e6(steps) and valid_path(path):
        levels = list_of_levels(path)
        #print(levels)
        print(countingValleys(steps, path))
