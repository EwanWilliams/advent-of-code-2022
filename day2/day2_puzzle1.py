def main():
    totalScore = 0
    with open("rps_strategy.txt", "r") as file:

        for line in file:
            cleanLine = line.rstrip("\n")
            rpsRound = cleanLine.split(" ")
            oppMove = normMove(rpsRound[0])
            plaMove = normMove(rpsRound[1])

            rndScore = moveScore(plaMove) + resultScore(oppMove, plaMove)
            totalScore += rndScore

            #print(oppMove, plaMove, rndScore)

    print("Total Score is: ", totalScore)


def moveScore(move):
    if move == "r":
        return 1
    elif move == "p":
        return 2
    else:
        return 3


def resultScore(opp, pla):
    if opp == pla:
        # if draw
        return 3
    elif (opp == "r" and pla == "s") or (opp == "p" and pla == "r") or (opp == "s" and pla == "p"):
        # if lose
        return 0
    else:
        # if win
        return 6


def normMove(move):
    if move == "A" or move == "X":
        return "r"
    elif move == "B" or move == "Y":
        return "p"
    else:
        return "s"


if __name__ == "__main__":
    main()