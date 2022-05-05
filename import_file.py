# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 18:58:51 2022

@author: TEJAS DESHPANDE
"""

def import_file():
    with open('Assembly_Code.txt') as f:
        text = f.read().splitlines() #array
        
    codes=[]

    for i in text:
        s=i.lower().strip()
        
        if '#' in s:
            index=s.index('#')
            s=s[:index]
        
        if len(s)==0:
            continue
        
        
        code=s.split(",")

        k=code[0].split()
        code.pop(0)
        code=k+code
        if code[0][len(code[0])-1]==":":
            codes.append([code[0]])
            code.pop(0)
        codes.append(code)

    return codes