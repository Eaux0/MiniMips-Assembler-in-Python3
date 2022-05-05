# MiniMips-Assembler-in-Python3

This is a program(written in Pyhton3) which simulates a two-pass MiniMIPS assembler

### The instructions implemented in the code are as following:-
#### A. R Type:
  1. Add: Adds value of two registers
  2. Sub: Subtracts value of two registers
  3. Or: Performs Or operation on two registers
  4. And: Performs And operation on two registers
  5. Xor: Performs Xor operation on two registers
  6. Slt: Compares two registers and puts 1 in the destination register if the first source register is smaller than second else puts 2.
#### B. I Type
  7. Addi: Adds a register and an immediate value
  8. Ori: Performs Or operation on a register and a immediate value
  9. Xori: Performs Xor operation on a register and a immediate value
  10. Slti: Compares a register and a immediate value and puts 1 in the destination register if the source register is smaller than immediate value else puts 2.
  11. Andi: Performs And operation on a register and an immediate value
#### C. J Type and Branch Type
  12. J: Jumps to a specific target which is given as label
  13. Bltz: Branch if the source register is smaller than 0
  14. Beq: Branch if the given registers are equal
  15. Bne: Branch if the given registers are not equa
