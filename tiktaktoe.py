#Experimentation
#Ongoing
import numpy as np

array01 = np.asarray([0,1,2,3,4,5,6,7,8],dtype = str) 
X = "X"
O = "O"
winningMoves = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),
             (1,4,7),(2,5,8),(0,4,8),(2,4,6))

def board():
    #Board 
    return("""
 ___ ___ ___
|   |   |   |
| {0} | {1} | {2} |
|---|---|---|
| {3} | {4} | {5} |
|---|---|---|
| {6} | {7} | {8} |
|___|___|___|
""".format(array01[0],array01[1],array01[2],array01[3],
           array01[4],array01[5],array01[6],array01[7],
           array01[8],))    

def question():
    global ans
    ans = None
    while ans not in ("X", "O"):
        ans = input("X or O?: ").upper()
        
question()        
        
def tik():
    #Correct Validation
    print(board())
    global userInput
    userInput = " "
    while userInput not in array01:       
        userInput = str(input("Place: "))
      
def placeTaken():
    #Is the space taken
    if array01[int(userInput)] != X or O:
        array01[int(userInput)] = ans 
    print(board())
       
def loop():
    while False in (array01 == "X") | (array01 == "O"):
        tik()
        placeTaken()
        print(array01)
    print("Tie")
        
loop()


