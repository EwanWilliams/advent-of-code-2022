def main():
    elfCalories = []
    currentSum = 0
    
    with open("elf_calorie_list.txt", "r") as file:
        for line in file:
            if line != "\n":
                currentSum += int(line)
            else:
                elfCalories.append(currentSum)
                currentSum = 0
                    
    top3Calories = sorted(elfCalories, reverse=True)[:3]
    top3Total = sum(top3Calories)            
    print("Total of top 3 elf calories: ", top3Total)


if __name__ == "__main__":
    main()