# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 19:33:57 2022

@author: TEJAS DESHPANDE
"""

def ishexadecimal(num):
    if num[0]=='0' and num[1]=='x':
        num=num[2:]
        
    for c in num:
        if not ((c<='9' and c>='0') or (c<='f' and c>='a')):
            return False
        
    return True