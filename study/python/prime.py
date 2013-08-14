#! /usr/bin/python 
#　-*- coding: utf-8 -*-


for i in range(1, 100):
    divided = False
    for j in range(2, i - 1):
        if i % j == 0:
            divided = True
    if not divided:
        print i




