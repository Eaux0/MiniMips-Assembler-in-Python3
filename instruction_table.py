# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 22:22:05 2022

@author: TEJAS DESHPANDE
"""

def instrcution_table():
    insTab={}
    v_name_tab={}
    var=[0]*32 #Registers -> $0 to $31 (initialized to 0) 
    
    #OPCODE TABLE:-

    #R Type Instructions
    insTab["add"]=(0,32)   #Add
    insTab["sub"]=(0,34)   #Subtract
    insTab["and"]=(0,36)   #AND
    insTab["or"]=(0,37)    #OR
    insTab["xor"]=(0,38)   #XOR
    insTab["slt"]=(0,42)   #Set Less Than
    
    
    #I Type Instructions
    insTab["addi"]=(8,-1)  #Add Immediate
    insTab["slti"]=(10,-1) #Set Less Than Immediate
    insTab["andi"]=(12,-1) #AND with Immediate
    insTab["ori"]=(13,-1)  #OR with Immediate
    insTab["xori"]=(14,-1) #XOR with Immediate
    
    
    #Jump Instructions
    insTab["j"]=(2,-1)     #Jump
    insTab["bltz"]=(1,-1)  #Branch Less Than Zero
    insTab["beq"]=(4,-1)   #Branch Equal 
    insTab["bne"]=(5,-1)   #Branch Not Equal
    
    
    #VARIABLE NAME TABLE:-
    v_name_tab['zero']=0
    v_name_tab['at']=1
    v_name_tab['v0']=2
    v_name_tab['v1']=3
    v_name_tab['a0']=4
    v_name_tab['a1']=5
    v_name_tab['a2']=6
    v_name_tab['a3']=7
    v_name_tab['t0']=8
    v_name_tab['t1']=9
    v_name_tab['t2']=10
    v_name_tab['t3']=11
    v_name_tab['t4']=12
    v_name_tab['t5']=13
    v_name_tab['t6']=14
    v_name_tab['t7']=15
    v_name_tab['s0']=16
    v_name_tab['s1']=17
    v_name_tab['s2']=18
    v_name_tab['s3']=19
    v_name_tab['s4']=20
    v_name_tab['s5']=21
    v_name_tab['s6']=22
    v_name_tab['s7']=23
    v_name_tab['t8']=24
    v_name_tab['t9']=25
    v_name_tab['k0']=26
    v_name_tab['k1']=27
    v_name_tab['gp']=28
    v_name_tab['sp']=29
    v_name_tab['fp']=30
    v_name_tab['ra']=31
    
    return insTab,var,v_name_tab