#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 08:20:24 2018

@author: pujan
"""
target = 999
sum = 0
for i in range(3,target):
    if(i%3 == 0) or (i%5==0):
        sum = i+sum
print("Sum: ", sum)
