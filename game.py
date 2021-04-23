import numpy as np
import random 
global gamearray 
global mCounter 
global playerturn
gamearray = np.zeros((2,2), dtype=int) #this initializes the array to 0s 

def minmax():
    n = random.randint(1,4)
    if n == 1 and gamearray[0][0] == 1:
        print("Already occupied, the minmax function will be called again")
        minmax()
        

    if n == 1 and gamearray[0][0] != 1:
        gamearray[0][0] = 2
        print("The computer picked : ")
        print(gamearray)
        return
        

    if n == 2 and gamearray[0][1] == 1:
        print("Already occupied, the minmax function will be called again")
        minmax()
        
    if n == 2 and gamearray[0][1] != 1:
        gamearray[0][1] = 2
        print("The computer picked : ")
        print(gamearray)
        return
    

    if n == 3 and gamearray[1][0] == 1:
        print("Already occupied, the minmax function will be called again")
        minmax()
    
    if n == 3 and gamearray[1][0] != 1:
        gamearray[1][0] = 2
        print("The computer picked : ")
        print(gamearray)
        return

    if n == 4 and gamearray[1][1] == 1:
        print("Already occupied, the minmax function will be called again")
        minmax()
        
    if n == 4 and gamearray[1][1] != 1:
        gamearray[1][1] = 2
        print("The computer picked : ")
        print(gamearray)
        return

    

    

def gameover():
    if ((gamearray[0][0] == 1 and gamearray[0][1] ==  1) or (gamearray[1][0] == 2 and gamearray[1][1] ==2) or (gamearray[0][0] == 1 and gamearray[0][1] == 1 and gamearray[1][0] == 1 and gamearray[1][1] == 1) or (gamearray[0][0] == 2 and gamearray[0][1] ==  2 and gamearray[1][0] == 2 and gamearray[1][1] == 2)):
        return True
    else:
        return False

print("Welcome to the TIC TAC TOE 2X2 Game by Usman Hamid")
print("As the human player you are assinged 1")
print("And the computer is assinged 2")
print("This is the layout of the game  :")
print(""" 1 | 2
 3 | 4""")
print("What the game looks like : ")
print(gamearray)

playerturn = 1
for i in range(4):
    if i == 0 or i == 2:
        hturn = int(input("Please input your turn (1,2,3,4):"))
        if hturn == 1:
            gamearray[0][0] = 1
        elif hturn == 2:
            gamearray[0][1] = 1
        elif hturn == 3:
            gamearray[1][0] = 1
        elif hturn == 4:
            gamearray[1][1] = 1
        print("You picked : ")
        print(gamearray)
    else:
        minmax()

        
    if gameover():
        break        
