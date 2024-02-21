#!/bin/python3
m = [0, ]  
c = 0
print("""BuBleFuck""")
l = ""
while l != ".stop":
    l = input('>>>')
    if l == ".clear": m = [0, ]
    else: 
        for i in l:
            if i == "&": m.append(0)
            if i == "!": c += 1
            if i == "%": c -= 1
            if i == "@": m[c] += 1
            if i == "$": m[c] -= 1
    print(*m, f"; cursor : {c}") 

        
