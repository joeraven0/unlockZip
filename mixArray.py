# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import itertools
array = ["apa","fisk","stereo","mongo"]

fisk=[]
temp = []
for x in range(1,5):
    fisk.append(array)
    iterables = fisk
    for t in itertools.product(*iterables):
        print("".join(t))
