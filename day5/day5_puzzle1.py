def main():
    crates = getStartPos()
    
    with open("crate_instructions.txt", "r") as file:
        for _ in range(10):
            next(file)

        for line in file:
            line = line.strip("move").replace("from", " ").replace("to", " ").strip()
            instructions = line.split("  ")
            crates = performInstr(crates, int(instructions[0]), int(instructions[1]) - 1, int(instructions[2]) - 1)
    
    topCrates(crates)


def performInstr(crates, quantity, currentStack, newStack):
    stack1 = crates[currentStack]
    stack2 = crates[newStack]

    for i in range(quantity):
        moving = stack1.pop()
        stack2.append(moving)
    
    crates[currentStack] = stack1
    crates[newStack] = stack2
    
    return crates


def topCrates(crates):
    onTop = []
    for i in crates:
        onTop.append(i.pop())
    
    print("Top crates are:")
    print(onTop)


def getStartPos():
    crates = [[],[],[],[],[],[],[],[],[]]

    with open("crate_instructions.txt", "r") as file:
        for i in range(8):
            lineStr = next(file).strip().lstrip("[").rstrip("]")
            line = lineStr.split("] [")
            for j in range(len(line)):
                if line[j] != " ":
                    crates[j].append(line[j])
    
    for i in range(len(crates)):
        crates[i].reverse()
    
    return crates


if __name__ == "__main__":
    main()