def main():
    with open("datastream.txt", "r") as file:
        data = file.readline()
    
    print(findStart(data))


def findStart(data):
    fourCount = 0
    lastFour = ["","","",""]
    index = 0
    for i in data:
        index += 1
        lastFour[fourCount] = i

        fourCount += 1
        if fourCount > 3:
            fourCount = 0
        
        if len(set(lastFour)) == len(lastFour):
            return index


if __name__ == "__main__":
    main()