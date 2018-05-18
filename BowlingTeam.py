#By Joshua Wells
#Bowling Team
#April 21, 2018
#CS 1400
"""requirements

The team average score, rounded down to the nearest pin.
Last, your program should write each of the lists and the summary information
to a text file called game_results.txt in the same format it is
displayed on the screen.
Your program should work with the following input:

Sam 200
Bill 125
Mary 235
Jane 205
Alex 300
Sue 280
"""
import sys


#I prefer this order of listing the players and scores, and I wanted to add extra ordered lists

def main():
    nameandScores, players, total, other = getScores()
    deletable = nameandScores
    listScores(nameandScores, players)
    alphaList, alphaList2 = alphabetical(nameandScores, players)
    highScoreList = highScore(nameandScores, players)
    lowScoreList = lowScore(highScoreList, players)
    highScorePeople, count = highScoreCongrats(highScoreList, players)
    lowScorePeople, count1 = lowScoreFail(lowScoreList, players)
    endMessage(highScorePeople, count, lowScorePeople, count1, total, players)
    saveFile(other, players, alphaList2, highScoreList, lowScoreList, highScorePeople, count, lowScorePeople, count1, total)
    #, alphaList, highScoreList, lowScoreList, highScorePeople, count, lowScorePeople, count1
#TODO: take all lists and make them variables in main so that they can be put in file

def getScores():
    nameandScores = []
    peopleList = []
    other = []
    total = 0
    nameandScore = "start"
    nameandScore = str(input("Enter the name and score of the next player: "))
    if nameandScore == "":     #Checks to see if the first entry is more than nothing
        input("You did not enter anything. Press enter to exit.")
        sys.exit()
    players = 0
    while nameandScore != "":
        try:            #This checks to see if values will work for future sorting
            int(nameandScore.split()[-1])
            total += int(nameandScore.split()[-1])
        except:
            print("Your name and score was not entered in the correct way.")
            input("Press enter to exit.")
            sys.exit()
        if int(nameandScore.split()[-1]) > 300 or int(nameandScore.split()[-1]) < 0:
            print("That score is not a possible bowling score.")
            input("Press enter to exit.")
            sys.exit()
        nameandScores.append(nameandScore)
        other.append(nameandScore)
        players += 1
        if players >= 2:    #I assume that at least two players will be entered
            print("If there are no more players press enter.")
        nameandScore = str(input("Enter the name and score of the next player: "))
    return nameandScores, players, total, other
    
def listScores(nameandScores, players):
    nameandScores2 = []
    print()
    print("Name and Score of each player in the order entered:")
    for i in range(players):
        if int(nameandScores[i].split()[-1]) == 300:
            nameandScores2.append("*" + nameandScores[i])
        else:
            nameandScores2.append(nameandScores[i])
    for i in range(players):
        print(nameandScores2[i])

def alphabetical(nameandScores, players):
    alphaList2 = []
    alphaList = sorted(nameandScores)
    print()
    print("Name and Score of each player in alphabetical order:")
    for i in range(players):
        if int(alphaList[i].split()[-1]) == 300:
            alphaList2.append("*" + alphaList[i])
        else:
            alphaList2.append(alphaList[i])
    for i in range(players):
        print(alphaList2[i])
    return alphaList, alphaList2

def highScore(nameandScores, players):
#TODO fix this crap
    print()
    print("Name and Score of each player from highest to lowest.")
    highScoreList = []
    nexthigh = 0
    position = 0
    for i in range(players):
        nexthigh = int(nameandScores[0].split()[-1])
        position = 0
        for i in range(len(nameandScores)):
            if nexthigh < int(nameandScores[i].split()[-1]):
                nexthigh = int(nameandScores[i].split()[-1])
                position = i
        highScoreList.append(nameandScores[position])
        del nameandScores[position]
    for i in range(players):
        if int(highScoreList[i].split()[-1]) == 300:
            highScoreList[i] = ("*" + highScoreList[i])
        else:
            None
    for i in range(players):
        print(highScoreList[i])
    return highScoreList

def lowScore(highScoreList, players):
    lowScoreList = []
    lowScoreList2 = []
    print()
    print("Name and Score of each player from Lowest Score to Highest Score:")
    for i in range(players -1, -1, -1):
        lowScoreList.append(highScoreList[i])
    for i in range(players):
        print(lowScoreList[i])
    return lowScoreList

def highScoreCongrats(highScoreList, players):
    highScorePeople = []
    highScorePeople2 = []
    count = 0
    for i in range(0,players):
        if int(highScoreList[0].split()[-1]) == int(highScoreList[i].split()[-1]):
            count += 1
    for i in range(count):
        highScorePeople.append(highScoreList[i])
    for i in range(count):
        if int(highScorePeople[i].split()[-1]) == 300:
            highScorePeople2.append("*" + highScorePeople[i])
        else:
            highScorePeople2.append(highScorePeople[i])
    return highScorePeople, count

def lowScoreFail(lowScoreList, players):
    lowScorePeople = []
    count1 = 0
    for i in range(0,players):
        if int(lowScoreList[0].split()[-1]) == int(lowScoreList[i].split()[-1]):
            count1 += 1
    for i in range(count1):
        lowScorePeople.append(lowScoreList[i])
    return lowScorePeople, count1
    
def endMessage(highScorePeople, count, lowScorePeople, count1, total, players):
    low = []
    high = []
    for i in range(count):
        high.append(highScorePeople[i].split()[0])
    for i in range(count1):
        low.append(lowScorePeople[i].split()[0])
    print()
    print("Congratulations to the winner(s): ", end="")
    for i in range(count):
        if count == 1:
            print(high[i])
        else:
            print(high[i], end="")
            print(",", end="")
    print()
    print("better luck next time: ", end="")
    for i in range(count1):
        if count1 == 1:
            print(low[i])
        else:
            print(low[i], end="")
            print(",", end="")
    print("the team average score was: ", total//players)

def saveFile(nameandScores, players, alphaList2, highScoreList, lowScoreList, highScorePeople, count, lowScorePeople, count1, total):
    outFile = open("C:\\Users\\Josh\\Documents\\Spring 2018 UVU\\CS 1400\\Projects\\game_results.txt", "w")
    outFile.write("Name and Score of each player in the order entered:")
    outFile.write("\n")
    for i in range(players):
        if int(nameandScores[i].split()[-1]) == 300:
            nameandScores.append("*" + nameandScores[i])
        else:
            nameandScores.append(nameandScores[i])
    for i in range(players):
        outFile.write(nameandScores[i])
        outFile.write("\n")

#alphalist
    outFile.write("\n")
    outFile.write("Name and Score of each player in alphabetical order:")
    for i in range(players):
        outFile.write(alphaList2[i])
        outFile.write("\n")

#high score list
    outFile.write("\n")
    outFile.write("Name and Score of each player from highest to lowest.")
    for i in range(players):
        outFile.write(highScoreList[i])
        outFile.write("\n")

#low score list
    outFile.write("\n")
    outFile.write("Name and Score of each player from Lowest Score to Highest Score:")
    for i in range(players):
        outFile.write(lowScoreList[i])
        outFile.write("\n")

    low = []
    high = []
    for i in range(count):
        high.append(highScorePeople[i].split()[0])
    for i in range(count1):
        low.append(lowScorePeople[i].split()[0])
    
#end message
    outFile.write("\n")
    outFile.write("Congratulations to the winner(s): ")
    for i in range(count):
        if count == 1:
            outFile.write(high[i])
        else:
            outFile.write(high[i])
            outFile.write(", ")

    outFile.write("\n")
    outFile.write("better luck next time: ")
    for i in range(count1):
        if count1 == 1:
            outFile.write(low[i])
        else:
            outFile.write(low[i])
            outFile.write(", ")

    outFile.write("\n")
    outFile.write("the team average score was: ")
    average = total//players
    average = str(average)
    outFile.write(average)
    
        

    
    
if __name__ == '__main__':
    main()

#, alphaList, highScoreList, lowScoreList, highScorePeople, count, lowScorePeople, count1
