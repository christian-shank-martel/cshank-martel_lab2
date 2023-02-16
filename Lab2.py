#!/usr/bin/env python3
#Author: christian shank-martel 
#AuthorID: cshank-martel
#Date:Feb 15 2023
#Program: Lab2.py
import sys
arguments = sys.argv
Prog = sys.argv[0]

def var_used():
    var1=sys.argv[1]
    var2=sys.argv[2]

    print("program: ", Prog)
    print("Variable 1: ", var1)
    print("Variable 2: ", var2)

if __name__ == "__main__":
    var_used()
