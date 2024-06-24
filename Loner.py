# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 12:34:58 2024

@author: Krzysztof
"""

import matplotlib.pyplot as plt
import numpy as np
import random

class PlaySpace:
    """Class for defining valid spaces that Pawns can move into"""
    def __init__(self, xCoord, yCoord, active):
        ## Define x and y coordinate of space
        self.xCoord = xCoord
        self.yCoord = yCoord
        self.active = active
        # self.pm = self.PawnMove(left, right, up, down)
        return

    def show(self):
        """Desplay the playspace on a grid"""
        ## If there is a pawn
        if self.active == True:
            ## Display Green circle
            plt.plot(self.xCoord, self.yCoord, 'o', color = "green", markersize = 15)
            plt.ylim(-3.3,3.3)
            plt.xlim(-3.3,3.3)
        else:
            ## Display Red Square
            plt.plot(self.xCoord, self.yCoord, 's', color = "red", markersize = 15)
            plt.ylim(-3.3,3.3)
            plt.xlim(-3.3,3.3)

def CreateGrid():
    ## Define x and y as numpy arrays
    
    coords = np.zeros([2, 49])
    for i in range(7): ## x values
        for j in range (7): ## y values
            coords[0, (7 * i) + j] = i - 3
            coords[1, (7 * i) + j] = j - 3

    return coords

coords = CreateGrid()

def SetUpGame():
    # plt.figure() #############################################################################################
    coordList = []
    value = 0
    for i in range(len(coords[0])):
    
        ## Define ValidSpace class for each coordinate position
        x = coords[0, i]
        y = coords[1, i]
        
        if (abs(x) * abs(y)) < 4:
            value += 1
            coordList.append(PlaySpace(x, y, True))
    
    del i, x, y ## Delete obsolete variables
       
    ##Deactivate centre pawn
    coordList[16].active = False
    
    # for obj in coordList: #############################################################################################
    #     obj.show()
    
    
    return coordList
coordList = SetUpGame()


    
# plt.show() #############################################################################################
    
def LeftMovers(x, y, i):
    ## Declare Variables
    x1 = x - 1
    x2 = x - 2
    decider = -1
    landing = -1
    
    ##Loop for all play spaces
    for j in range(len(coordList)):
        ## If Coordinates exist & Active
        if (getattr(coordList[j],'xCoord') == x1) & (getattr(coordList[j],'yCoord') == y) & (getattr(coordList[j],'active') == True):
            # print(j, "move left decider pawn")
            decider = j
        ## If Coordinates exist & Empty
        if (getattr(coordList[j],'xCoord') == x2) & (getattr(coordList[j],'yCoord') == y) & (getattr(coordList[j],'active') == False):
            # print(j, "PAwn name of the landing pawn")
            landing = j
    ## If valid move return coordinate
    if (decider != -1) & (landing != -1):
        route = [i, decider, landing]
        return route   
def RightMovers(x, y, i):
    ## Declare Variables
    x1 = x + 1
    x2 = x + 2
    decider = -1
    landing = -1
    
    ##Loop for all play spaces
    for j in range(len(coordList)):
        ## If Coordinates exist & Active
        if (getattr(coordList[j],'xCoord') == x1) & (getattr(coordList[j],'yCoord') == y) & (getattr(coordList[j],'active') == True):
            # print(j, "move left decider pawn")
            decider = j
        ## If Coordinates exist & Empty
        if (getattr(coordList[j],'xCoord') == x2) & (getattr(coordList[j],'yCoord') == y) & (getattr(coordList[j],'active') == False):
            # print(j, "PAwn name of the landing pawn")
            landing = j
    ## If valid move return coordinate
    if (decider != -1) & (landing != -1):
        route = [i, decider, landing]
        return route

def DownMovers(x, y, i):
    ## Declare Variables
    y1 = y - 1
    y2 = y - 2
    decider = -1
    landing = -1
    
    ##Loop for all play spaces
    for j in range(len(coordList)):
        ## If Coordinates exist & Active
        if (getattr(coordList[j],'xCoord') == x) & (getattr(coordList[j],'yCoord') == y1) & (getattr(coordList[j],'active') == True):
            # print(j, "move left decider pawn")
            decider = j
        ## If Coordinates exist & Empty
        if (getattr(coordList[j],'xCoord') == x) & (getattr(coordList[j],'yCoord') == y2) & (getattr(coordList[j],'active') == False):
            # print(j, "PAwn name of the landing pawn")
            landing = j
    ## If valid move return coordinate
    if (decider != -1) & (landing != -1):
        route = [i, decider, landing]
        return route

def UpMovers(x, y, i):
    ## Declare Variables
    y1 = y + 1
    y2 = y + 2
    decider = -1
    landing = -1
    
    ##Loop for all play spaces
    for j in range(len(coordList)):
        ## If Coordinates exist & Active
        if (getattr(coordList[j],'xCoord') == x) & (getattr(coordList[j],'yCoord') == y1) & (getattr(coordList[j],'active') == True):
            # print(j, "move left decider pawn")
            decider = j
        ## If Coordinates exist & Empty
        if (getattr(coordList[j],'xCoord') == x) & (getattr(coordList[j],'yCoord') == y2) & (getattr(coordList[j],'active') == False):
            # print(j, "PAwn name of the landing pawn")
            landing = j
    ## If valid move return coordinate
    if (decider != -1) & (landing != -1):
        route = [i, decider, landing]
        return route
    
def FindMoves(coordList):
    ## Array for all valid moves
    moves = []
    for i in range(len(coordList)):
        if getattr(coordList[i],'active') == True:
            x = coordList[i].xCoord
            y = coordList[i].yCoord
            
            ## Identify Pawns that can move left in array
            left = LeftMovers(x, y, i)
            if left != None:
                ## Store Left moving pawns in array "moves"
                moves.append(left)  
            ## Identify Pawns that can move right in array
            right = RightMovers(x, y, i)
            if right != None:
                ## Store Right moving pawns in array "moves"
                moves.append(right)
            ## Identify Pawns that can move down in array
            down = DownMovers(x, y, i)
            if down != None:
                ## Store down moving pawns in array "moves"
                moves.append(down)
            ## Identify Pawns that can move up in array
            up = UpMovers(x, y, i)
            if up != None:
                ## Store up moving pawns in array "moves"
                moves.append(up)
    return moves

def MovePawn(validMoves):
    ## Pick move
    ##################    Random number generator to find move          ##################
    rand = random.randint(0,len(validMoves)-1)
    
    ## declare variables depending on chosen random number
    currentPawn = validMoves[rand][0]
    deciderPawn = validMoves[rand][1]
    finalPawn = validMoves[rand][2]
    
    ## Update attributes of Pawns
    setattr(coordList[currentPawn],'active', False)
    setattr(coordList[deciderPawn],'active', False)
    setattr(coordList[finalPawn],'active', True)
    
    ## Return chosen rand for future repeats
    return rand

def GamePlayer():
    """Function which plays a round of the game returning the numbers of Pawns left"""
    ## Declare variables
    move = []
    validMoves = FindMoves(coordList)  
    pawnsLeft = []
    
    ## While valid moves still exist
    while len(validMoves) != 0:
        
        ## Display moves Code #############################################################################################
        # for obj in coordList:
        #     obj.show()
        # plt.show()
        
        move.append(MovePawn(validMoves))
        validMoves = FindMoves(coordList)
        
    ##Loop for all play spaces
    for i in range(len(coordList)):
        ## If pawn is active
        if (getattr(coordList[i],'active') == True):
            ## Add active pawn to pawnsLeft list
            pawnsLeft.append(i)
    ## Display moves Code #############################################################################################
    # for obj in coordList:
    #     obj.show()
    # plt.show()
    return len(pawnsLeft), move

pawnLeft, move = GamePlayer()

genPawnLeft = []
while pawnLeft != 1:
    coordList = SetUpGame()
    
    pawnLeft, move = GamePlayer()
    genPawnLeft.append(pawnLeft)
print("Completed in ", len(genPawnLeft), " moves. with final solution = ", move)
