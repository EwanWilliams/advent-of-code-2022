def main():
    with open("datastream.txt", "r") as file:
        data = file.readline()
    
    print(findStart(data))


def findStart(data):
    fourteenCount = 0
    lastFourteen = ["","","","","","","","","","","","","",""]
    index = 0
    for i in data:
        index += 1
        lastFourteen[fourteenCount] = i

        fourteenCount += 1
        if fourteenCount > 13:
            fourteenCount = 0
        
        if len(set(lastFourteen)) == len(lastFourteen):
            return index


if __name__ == "__main__":
    main()