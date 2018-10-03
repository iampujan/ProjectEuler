#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 08:57:44 2018

@author: pujan
"""
#Find the sum of all the even valued terms in the Fibonacci sequence which do not exceed four million.

e = 4000000
sum = 0
a = 1
b = 1
if b<e:
    if(b % 2 ==0):
        sum = sum+b
    c = a+b
    a=b
    b=c
print(sum)
