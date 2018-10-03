#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 22:14:19 2018

@author: mrrobot
"""
def check_palindrome(s):
    if s == s[::-1]:
        return True
product_pal = []

for i in range(999,910,-1):
    for j in range(999,910,-1):
        product = i*j
        if check_palindrome(str(product)):
            product_pal.append(product)
            print ("i=", i,"j = ",j, "for", product)
print(max(product_pal))
        