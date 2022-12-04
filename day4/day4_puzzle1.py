def main():
    totalFullContain = 0

    with open("assignment_pairs.txt", "r") as file:
        for line in file:
            line = line.rstrip("\n")
            pair = line.split(",")
            
            if fullContain(pair) == True:
                totalFullContain += 1
    
    print("Total assignment pairs that fully contain each other: ", totalFullContain)


def fullContain(pair):
    elf1 = str(pair[0]).split("-")
    elf2 = str(pair[1]).split("-")

    if int(elf1[0]) <= int(elf2[0]) and int(elf1[1]) >= int(elf2[1]):
        return True
    elif int(elf2[0]) <= int(elf1[0]) and int(elf2[1]) >= int(elf1[1]):
        return True
    else:
        return False

if __name__ == "__main__":
    main()