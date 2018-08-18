#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 08:20:24 2018

@author: pujan
"""
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

target = 1000
sum = 0
for i in range(3,target):
    if(i%3 == 0 or i%5 == 0):
        sum = sum+i
print("Sum: ", sum)
