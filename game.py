import numpy
import random 

print("\nWelcome to the Tic-Tac-Toe 2x2 Game")

print(" The Human Player is assinged X. ")
print(" The Computer is assinged O. ")
print("\n Pick your Specified Place according to the Given Numbers. You can also Override. ")
print(" The First Player to Occupy any of the Three Places, would Win")
print(""" 
    1 | 2
    3 | 4
    """)


def human_turn():
    
    m = int(input("\nInput where to Mark (1,2,3,4): "))
        
    if m == 1:
        gamearray[0][0] = 'X'
    elif m == 2:
        gamearray[0][1] = 'X'
    elif m == 3:
        gamearray[1][0] = 'X'
    elif m == 4:
        gamearray[1][1] = 'X'
    else:
        human_turn()
    
    print("You Picked: ")
    print(gamearray)
    return


def cpu_turn():
    
    p = random.randint(1,4)

    if p == 1:
        gamearray[0][0] = 'O'
        
    elif p == 2:
        gamearray[0][1] = 'O'
        
    elif p == 3:
        gamearray[1][0] = 'O'
        
    elif p == 4:
        gamearray[1][1] = 'O'
    else:
        cpu_turn()
    
    print("\nThe Computer Picked: ")
    print(gamearray)
    return


def gameover():
    
    if(
        (gamearray[0][0] == 'X' and gamearray[0][1] ==  'X' and gamearray[1][0] == 'X') or # 1 2 3
        (gamearray[0][0] == 'X' and gamearray[0][1] ==  'X' and gamearray[1][1] == 'X') or # 1 2 4
        (gamearray[0][0] == 'X' and gamearray[1][0] ==  'X' and gamearray[1][1] == 'X') or # 1 3 4
        (gamearray[0][1] == 'X' and gamearray[1][0] ==  'X' and gamearray[1][1] == 'X')    # 2 3 4
    ):
        print("\n You Won!")
        return True
    
    elif( 
        (gamearray[0][0] == 'O' and gamearray[0][1] ==  'O' and gamearray[1][0] == 'O') or # 1 2 3
        (gamearray[0][0] == 'O' and gamearray[0][1] ==  'O' and gamearray[1][1] == 'O') or # 1 2 4
        (gamearray[0][0] == 'O' and gamearray[1][0] ==  'O' and gamearray[1][1] == 'O') or # 1 3 4
        (gamearray[0][1] == 'O' and gamearray[1][0] ==  'O' and gamearray[1][1] == 'O')    # 2 3 4
    ):
        print("\n You Lose!")
        return True

    else:
        return False



#The Main Function

gamearray = numpy.zeros((2,2), dtype=str)
print(gamearray)

turn = random.randint(0,1)
if turn == 0:
    print("\n Your Turn First! ")
elif turn == 1:
    print("\n The Computer goes First! ")


while(True):
    
    if turn%2 == 0:
        human_turn()
    else:
        cpu_turn()
    
    turn+=1

    if gameover():
        break        


print("\n\n")

