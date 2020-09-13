#Made by Infinite-Program

"""
    NOTE:

-The "for loop" repeats its loop body for each element of the sequence.
-All sequences are made up of elements. (Like elements in a list.)

"""
 
#-------------------------------------------------------------------------

#Basic "for loop" introduction

def basic():
    
    word = input("Word: ")
    #"i" is a variable
    for i in word:
        #The variable "i" gets each successive element
        #The loop will iterate over a sequence one at a time
        print(i) 
    
#basic()

#-------------------------------------------------------------------------

#Counting Program (Use of "range")

#end= " " keeps the output on the same line

def ra():
    
    #This loop will start counting form 0 as
    #all computers count from 0
    print("I will count your number.")
    number = int(input("Number: "))
    #range(Start point, End point(users choice))
    for i in range(1,number+1):
        #end=" " will put all my elements on the same line
        print(i, end=" ")
        
    #This loop will count in interations of x
    print("\n")
    print("Tell me what to count in.")
    multiplyer = int(input("Multiplyer: "))
    print("\nI will count {0} in {1}s.".format(number,multiplyer))
    #range(Start point, Number(End point), Step)
    for i in range(0,number+1,multiplyer):
        if i == 0:
            continue
        print(i, end=" ")
    
    print("\n")
    print("I will count your original number backwards.")
    #range(Start , End Point, Step)
    for i in range(number,0,-1):
        print(i, end=" ")
        
#ra()
