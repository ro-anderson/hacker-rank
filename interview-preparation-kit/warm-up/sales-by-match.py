import math
import os
import random
import re
import sys

def count_freq_in_list(num, ar):
count = 0
for elem in ar:

    if elem == num:
        count +=1
return count

def get_dict_with_freqs(ar):
        dict_freq = {num: count_freq_in_list(num, ar) for num in set(ar)}
        return dict_freq

def btw1and100(n):
    if n >=1 and n <= 100:
        return True
    return False

def check_ar(ar):
    for elem in ar:
        if not btw1and100(elem):
            return False
    return True
            
def sockMerchant(n, ar):
    # constrains
    if btw1and100(n) and check_ar(ar):
        dict_freq = get_dict_with_freqs(ar) 
        pairs_per_element = [x // 2 for x in dict_freq.values()]
        return sum(pairs_per_element) 

if __name__ == '__main__':

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)
    print(result)
	
