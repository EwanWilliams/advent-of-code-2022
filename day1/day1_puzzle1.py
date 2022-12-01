def main():
    highestCalorie = 0
    currentSum = 0

    with open("elf_calorie_list.txt", "r") as file:
        for line in file:
            if line == "\n":
                if currentSum > highestCalorie:
                    highestCalorie = currentSum
                    currentSum = 0
                else:
                    currentSum = 0
            else:
                currentSum += int(line)
            
        print("Highest calorie count is: ", highestCalorie)    


if __name__ == "__main__":
    main()