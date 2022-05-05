# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 15:13:48 2022

@author: TEJAS DESHPANDE
"""

def processing(code,var):
    
    def r_type(ins):
      sr1=int(ins[6:11],2)  #Source Register 1
      sr2=int(ins[11:16],2)  #Source Register 2
      dr=int(ins[16:21],2)  #Destination Register
      shift=int(ins[21:26],2)  #Shift amount
      op_ext=int(ins[26:32],2)  #Opcode Extension
      
      if dr==0:
          return
      
      if op_ext==32:
          var[dr]=var[sr1] + var[sr2]
      elif op_ext==34:
          var[dr]=var[sr1] - var[sr2]
      elif op_ext==36:
          var[dr]=var[sr1] & var[sr2]
      elif op_ext==37:
          var[dr]=var[sr1] | var[sr2]
      elif op_ext==38:
          var[dr]=var[sr1] ^ var[sr2]
      elif op_ext==42:
          var[dr]=1 if var[sr2]>var[sr1] else 0
        
    def i_type(ins):
        opcode=int(ins[0:6],2)  #Opcode
        sr=int(ins[6:11],2)  #Source Register 
        dr=int(ins[11:16],2)  #Destination Register
        i_val=int(ins[16:],2)  # Immediate Value
        
        if dr==0:
            return
        
        #print(opcode," ",sr," ",dr," ",i_val)
        
        if opcode==8:
            var[dr]=var[sr]+i_val
        elif opcode==10:
            var[dr]=1 if var[sr]<i_val else 0
        elif opcode==12:
            var[dr]=var[sr] & i_val
        elif opcode==13:
            var[dr]=var[sr] | i_val
        elif opcode==14:
            var[dr]=var[sr] ^ i_val
    
    def j_type(ins,i):
        opcode=int(ins[0:6],2)  #Opcode
        if opcode==2:
            Label=int(ins[6:],2) #Returning Label
            return Label-1
        elif opcode==1:
            sr=int(ins[6:11],2)  #Source Register
            Label=int(ins[11:],2)#Returning Label
            if var[sr]<0:
                return Label-1
            else:
                return i
        elif opcode==4 or opcode==5:
            sr1=int(ins[6:11],2)   #Source Register 1
            sr2=int(ins[11:16],2)  #Source Register 2
            Label=int(ins[16:],2) #Returning Label
            if opcode==4:
                if var[sr1]==var[sr2]:
                    return Label-1
                else:
                    return i
            if opcode==5:
                if var[sr1]==var[sr2]:
                    return i
                else:
                    return Label-1
            
    i=0
    while i<len(code):
        inst=code[i]
        ins=inst[0]
        
        opcode=int(ins[:6],2)
        
        if opcode==0:
            r_type(ins)
        elif opcode>7 and opcode<15:
            i_type(ins)
        elif opcode==2 or opcode==1:
            i=j_type(ins,i)
        i+=1
    return var