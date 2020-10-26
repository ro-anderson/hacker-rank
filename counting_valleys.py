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

def can_be_valley(path, idx):
    if path[idx] == 0 and path[idx + 1] == -1:
        return True
    return False

def is_valley(path, idx):
    count = idx + 1
    while count < len(path):
        if path[count] == 0:
            return  True
    return False

def list_of_levels(path):
    idx = 0
    levels = []

    for step in list(path):
        if idx == 0:
            levels.append(0)
            levels.append(step_value(step))

        elif idx + 1 < len(path):
            levels.append(levels[idx] + step_value(step))
        idx += 1
    return levels
path = 'UDDDDDD'
levels = list_of_levels(path)

def countingValleys(steps, path):
    levels = list_of_levels(path)
    idx = 0
    valleys = 0
    for level in levels:
        if can_be_valley(path,idx):
            if is_valley(path, idx):
                valleys += 1
        idx += 1
    return valleys

if __name__ == '__main__':
    steps = int(input().strip())
    path = input()

    if btw2and10e6(steps) and valid_path(path):
        print(countingValleys(steps, path))
