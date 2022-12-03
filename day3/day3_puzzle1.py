def main():
    sumPriority = 0

    with open("rucksack_list.txt", "r") as file:
        for line in file:
            line = line.rstrip("\n")
            comp1 = line[:int(len(line)/2)]
            comp2 = line[int(len(line)/2):]

            cItem = findCommonItem(comp1, comp2)
            sumPriority += itemPriority(cItem)
    
    print("Total priority of items common between compartments: ", sumPriority)
        

def itemPriority(item):
    p = ord(item) - 38
    if p < 53:
        return p
    else:
        return p - 58


def findCommonItem(comp1, comp2):
    for i in comp1:
        for j in comp2:
            if i == j:
                return i


if __name__ == "__main__":
    main()