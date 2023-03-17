# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 14:30:22 2021

@author: VAIO
"""
from backward_chaining import standardize_variables, add_to_kb, fol_bc_ask

fn="input.txt"
queries = []
knowledge_base = []
f1=open(fn, "r")
input = f1.readlines()
input = [x.strip() for x in input]

for i in range(1, int(input[0]) + 1): 
    queries.append(input[i].replace(" ", ""))
for i in range(int(input[0]) + 2, int(input[int(input[0]) + 1]) +
int(input[0]) + 2):
    knowledge_base.append(input[i].replace(" ", ""))
knowledge_base = standardize_variables(knowledge_base)

kb = {}
list_of_predicates = []
add_to_kb(knowledge_base)

fileOut = open("output.txt", "w")
for query in queries:
    result = fol_bc_ask(query, {})
    if result != None:
        print("True", result)
        fileOut.write("TRUE" + "\n")
        else:
            print("False", result)
            fileOut.write("FALSE" + "\n")
            
fileOut.close()
f1.close