# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 19:00:08 2022

@author: TEJAS DESHPANDE
"""
import sys
import import_file
import instruction_table as it
import ishex
import processing as p

codes=import_file.import_file()
insTab,var,v_name_tab=it.instrcution_table()
labTab={}

codes=[x for x in codes if x!=[]]    #Removing all Empty cells
print()
for k in codes:
    print(k)

def first_pass(codes):
    labTab={}
    linec=0
    
    for s in codes:
        if s[0][-1]!=":" and len(s)==1:
            sys.exit(f"Unidentified keyword: \"{s[0]}\"")
        if s[0][-1]==":":
            k=s[0][:-1]
            labTab[k]=linec
                
        for i in range(len(s)):
            s[i]=s[i].strip()
            if i==3:
                if s[i] in labTab:
                    continue
                if s[i][0]=='$':
                    continue
                if s[i].isnumeric() or ishex.ishexadecimal(s[i]):
                    continue
                labTab[s[i]]=-1
                
        linec+=1

    for k in labTab:
        if labTab[k]==-1:
            sys.exit(f"Unidentified keyword: \"{k}\"")
                
    return labTab

def second_pass(codes, labTab):
    linec=0
    
    for ins in codes:
        linec+=1
        
        if len(ins)==1:
            ins[0]=('LAB', labTab[ins[0][:-1]])
            continue
        
        for i in range(len(ins)):
            if ins[i] in insTab:
                ins[i]=insTab[ins[i]]
            
            elif ins[i][0]=='$':
                reg_num=(ins[i][1:])
                if reg_num in v_name_tab:
                    ins[i]=('REG', v_name_tab[reg_num])
                elif int(reg_num)>=0 and int(reg_num)<32:
                    ins[i]=('REG', int(reg_num))
                else:
                    sys.exit(f"Registers Numbers only from 0 to 31, (line: {linec})")
           
            elif ins[i].isnumeric():
                ins[i]=('CON', int(ins[i]))
            
            elif ishex.ishexadecimal(ins[i]):
                k=int(ins[i],base=16)
                ins[i]=('CON', k)
            
            elif ins[i] in labTab:
                ins[i]=('LAB', labTab[ins[i]])
                
            if type(ins[i])!=tuple and ins[i][:-1] not in labTab:
                sys.exit(f"Unidentified keyword: \"{ins[i]}\" on line {linec}")
            
            
    print("\n")
    for k in codes:
        print(k)
        
def tuple_to_machinelanguage(codes, labTab):
    binary_codes=[]
    for ins in codes:
        
        if len(ins)==1:
            continue
        
        curr_line=""
        
        if ins[0][0]==0:     #R Type Instruction
            curr_line+=format(ins[0][0],"06b")  #Opcode
            curr_line+=format(ins[2][1],"05b")  #Source Register 1
            curr_line+=format(ins[3][1],"05b")  #Source Register 2
            curr_line+=format(ins[1][1],"05b")  #Destination Register
            curr_line+=format(ins[0][0],"05b")  #Shift amount
            curr_line+=format(ins[0][1],"06b")  #Opcode Extension
            
        elif ins[0][1]==-1:  #I Type Instruction
            curr_line+=format(ins[0][0],"06b")  #Opcode
            if ins[0][0]==2:
                curr_line+=format(ins[1][1],"026b")
            elif ins[0][0]==4 or ins[0][0]==5:
                curr_line+=format(ins[1][1],"05b")  #Source Register 1
                curr_line+=format(ins[3][1],"05b")  #Source Register 2
                curr_line+=format(ins[2][1],"016b") #Label
            elif ins[0][0]==1:
                curr_line+=format(ins[1][1],"05b")  #Destination Register
                curr_line+=format(ins[2][1],"021b") #Label
            else:
                curr_line+=format(ins[2][1],"05b")  #Source Register
                curr_line+=format(ins[1][1],"05b")  #Destination Register
                curr_line+=format(ins[3][1],"016b") #Immediate Value
                
        elif ins[0][1]==-2:  #J Type Instruction
            curr_line+=format(ins[0][0],"06b")  #Opcode
            curr_line+=format(ins[2][1],"05b")  #Source Register
            curr_line+=format(ins[1][1],"05b")  #Destination Register
            curr_line+=format(ins[3][1],"016b") #Immediate Value
            
        
        binary_codes.append([curr_line])
    
    codes=binary_codes
    
    print("\n")
    for k in codes:
        print(k)
        
    return codes


labTab=first_pass(codes)
print("\n")
for i in labTab:
    print(i," -> ",labTab[i])
second_pass(codes, labTab)
codes=tuple_to_machinelanguage(codes,labTab)
v_final=p.processing(codes,var)

print("\n")
print("$0 -> 0")
for i in range(1,32):
    if v_final[i]==0:
        continue
    print(f"${i} -> {v_final[i]}")