#!/bin/python3

memory = [0, ]  

cursor = 0

def main(line):
    global cursor, memory
    
    for i in line:
        if i == "&":
            memory.append(0)

        if i == "!":
            cursor += 1

        if i == "%":
            cursor -= 1

        if i == "@":
            memory[cursor] += 1

        if i == "$":
            memory[cursor] -= 1


if __name__ == "__main__":
    print("""\nA very useless programming language!\n""")
    line = ""
    while line != ".stop":
        line = input('>>>')
        if line == ".clear":
            memory = [0, ]
            continue
        
        else:
            main(line)
            print(*memory)
            print(cursor, ': cursor')        
        

