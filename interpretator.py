#!/bin/python3

"""
BuBlefuck 

commands:
    & - make new point
    ! - next point
    % - previous point
    @ - add 1 to the current point
    $ - remove 1 of the current point

"""

memory = [0, ]

def add(current_point):
    logs = f"{current_point} + 1"
    memory[current_point] += 1
    return logs

def remove(current_point):
    logs = f"{current_point} - 1"
    memory[current_point] -= 1
    return logs

def check_next_point(current_point):
    logs = f"{current_point} -> next"
    try:
        memory[current_point + 1]
    except:
        raise MemoryError

    return logs

def check_back_point(current_point):
    logs = f"{current_point} -> back"
    try:
        memory[current_point + 1]
    except:
        raise MemoryError

    return logs

def add_point():
    memory.append(0)
    return "new point"


def main(line):
    current_point = 0
    for i in line:
        if i == "&":
            print(add_point())

        if i == "!":
            print(check_next_point(current_point))
            current_point += 1

        if i == "%":
            print(check_back_point(current_point))
            current_point -= 1

        if i == "@":
            print(add(current_point))

        if i == "$":
            print(remove(current_point))


if __name__ == "__main__":
    print("""
    
      A very useless programming language! 
    
    """)
    line = input('>>>')
    while line != "stop":
        main(line)
        print(f"-------------{len(memory)}-points-were-used-------------------------")
        print(*memory)
        line = input('>>>')

