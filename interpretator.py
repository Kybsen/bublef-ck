#!/bin/python3
memory = [0, ]  
cursor = 0
print("""\nBuBleFuck\n""")
line = ""
while line != ".stop":
    line = input('>>>')
    if line == ".clear": memory = [0, ]
    else: 
        for i in line:
            if i == "&": memory.append(0)
            if i == "!": cursor += 1
            if i == "%": cursor -= 1
            if i == "@": memory[cursor] += 1
            if i == "$": memory[cursor] -= 1

    print(*memory, f"; cursor : {cursor}") 
