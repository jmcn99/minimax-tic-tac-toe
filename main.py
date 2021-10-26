import random
import copy
#Player = O


board = [[" "," "," "],[" "," "," "],[" "," "," "]]
game = True

def printBoard(b):
    print("\n\n")
    print(f"{b[0][0]}|{b[0][1]}|{b[0][2]}")
    print("- - -")
    print(f"{b[1][0]}|{b[1][1]}|{b[1][2]}")
    print("- - -")
    print(f"{b[2][0]}|{b[2][1]}|{b[2][2]}")

def makeMove(b, xy, player):
    if player == True:
        s = "o"
    else:
        s = "x"
    b[xy[0]][xy[1]] = s
    printBoard(b)

def getInput():
    xy = tuple(int(x.strip()) - 1 for x in input("Please enter x,y coordinates for your move (ex, '2,3'): ").split(','))
    return xy

def getScore(b):

    for x in range(0, 3):
        if b[x][0] == b[x][1] and b[x][1] == b[x][2]:
            if b[x][0] == "x":
                return 10
            if b[x][0] == "o":
                return -10

    for y in range (0, 3):
        if b[0][y] == b[1][y] and b[1][y] == b[2][y]:
            if b[0][y] == "x":
                return 10
            if b[0][y] == "o":
                return -10

    if b[0][0] == b[1][1] and b[1][1] == b[2][2]:
        if b[0][0] == "x":
            return 10
        if b[0][0] == "o":
            return -10
    
    if b[0][2] == b[1][1] and b[1][1] == b[2][0]:
        if b[1][1] == "x":
            return 10
        if b[1][1] == "o":
            return -10
    
    return 0

"""
def getMoves(b, isX):
    possibleMoves = []
    for x in range(0,3):
        for y in range(0,3):
            if b[x][y] == " ":
                tempBoard = copy.deepcopy(b)
                if isX:
                    tempBoard[x][y] = "x"
                else:
                    tempBoard[x][y] = "o"
                possibleMoves.append(tempBoard)
    return possibleMoves
"""

def movesLeft(b):
    for x in range(0,3):
        for y in range(0,3):
            if b[x][y] == " ":
                return True
    return False

def minimax(b, depth, isMax):
    #Check base case, see if someone won or tie
    if movesLeft(b) == False:
        return getScore(b)

                
    #printBoard(b)
    if isMax:
        maxEval = float("-Inf")

        for x in range(0,3):
            for y in range(0,3):
                if b[x][y] == " ":
                    b[x][y] = "x"
                    eval = minimax(b, depth + 1, False)
                    maxEval = max(maxEval, eval) - depth
                    b[x][y] = " "
        return maxEval
    
    else:
        minEval = float("Inf")
       
        for x in range(0,3):
            for y in range(0,3):
                if b[x][y] == " ":
                    b[x][y] = "o"
                    eval = minimax(b, depth + 1, True)
                    minEval = min(minEval, eval) + depth
                    b[x][y] = " "
        return minEval

def getBestMove(b, isMax):
    bestMove = None
    if isMax == True:
        bestScore = float("-Inf")
    else: 
        bestScore = float("Inf")
    for x in range(0,3):
        for y in range(0,3):
            if b[x][y] == " ":
                if isMax == True:
                    b[x][y] = "x"
                else:
                    b[x][y] = "o"
                tempScore = minimax(b, 0, not isMax) 
                print(tempScore)
                b[x][y] = " "
                if isMax == True:
                    if tempScore > bestScore:
                        bestScore = tempScore
                        bestMove = (x,y)
                else:
                    if tempScore < bestScore:
                        bestScore = tempScore
                        bestMove = (x,y)
    print(bestMove)
    return bestMove


def play():

    while True:
        if getScore(board) == 10:
            print("AI Wins!")
            break
        elif getScore(board) == -10:
            print("Player Wins!")
            break
        elif getScore(board) == 0 and movesLeft(board) == False:
            print("Tie!")
            break

        #Random starting player


        #makeMove(board, getInput(), True)
        makeMove(board, getBestMove(board, True), False)
        makeMove(board, getBestMove(board, False), True)
       
        
        

def test():
    board = [["x"," ","o"],
            ["x","x","o"],
            ["o"," "," "]]
    print(getBestMove(board, True))

play()