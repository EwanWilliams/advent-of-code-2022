def main():
    sumPriority = 0
    data = []

    with open("rucksack_list.txt", "r") as file:
        for line in file:
            data.append(line.rstrip("\n"))

    gi= 0
    for i in range(int(len(data)/3)):
        bag1 = data[gi]
        gi += 1
        bag2 = data[gi]
        gi += 1
        bag3 = data[gi]
        gi += 1

        cItem = findCommonItem(bag1, bag2, bag3)
        sumPriority += itemPriority(cItem)

    print("Total priority of group badges: ", sumPriority)


def itemPriority(item):
    p = ord(item) - 38
    if p < 53:
        return p
    else:
        return p - 58


def findCommonItem(bag1, bag2, bag3):
    for i in bag1:
        for j in bag2:
            for k in bag3:
                if i == j and i == k:
                    return i


if __name__ == "__main__":
    main()