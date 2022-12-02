def main():
    totalScore = 0
    with open("rps_strategy.txt", "r") as file:

        for line in file:
            cleanLine = line.rstrip("\n")
            rpsRound = cleanLine.split(" ")
            oppMove = normMove(rpsRound[0])
            outcome = normOut(rpsRound[1])
            plaMove = whatMove(oppMove, outcome)
            
            rndScore = moveScore(plaMove) + resultScore(oppMove, plaMove)
            totalScore += rndScore

            #print(oppMove, plaMove, outcome, rndScore)


    print("Total Score is: ", totalScore)


def whatMove(opp, out):
    if out == "d":
        return opp
    elif out == "l":
        if opp == "r":
            return "s"
        elif opp =="p":
            return "r"
        else:
            return "p"
    else:
        if opp == "r":
            return "p"
        elif opp =="p":
            return "s"
        else:
            return "r"

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

def moveScore(move):
    if move == "r":
        return 1
    elif move == "p":
        return 2
    else:
        return 3

def normOut(out):
    if out == "X":
        return "l"
    elif out == "Y":
        return "d"
    else:
        return "w"

def normMove(move):
    if move == "A" or move == "X":
        return "r"
    elif move == "B" or move == "Y":
        return "p"
    else:
        return "s"


if __name__ == "__main__":
    main()