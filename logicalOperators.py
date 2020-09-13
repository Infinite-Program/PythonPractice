#Made by Infinite-Program
#Interpreting a value as True or False

#-------------------------------------------------------------------------

"""
    Note:

-The rules for what makes a value True or False are simple.
-The basic principal is this:
    -Any empty or Zero value is False
    -Everything else is True
-So 0 evaluates to False and any other number evaluates to True.
-(Negative values also evaluate to True)
-The empty string "" is False while any other string is True.
 
"""
#-------------------------------------------------------------------------

#False untill True

def m():
    print("Welcome to  the resturaunt.")
    print("There is a long wait.")
    print("Would you like to give us a tip?")
    money = int(input("Slip: "))
    #"money" is False untill the variable is updated
    if money:
    #This block will only run if "money" is updated to True
        #It will only be True if the user inputs anything above 0
        print("Ah, I think there is a tabel this way.")
    else:
        print("Please, sit. It may be a while. ")
#m()

#-------------------------------------------------------------------------

#Basic input validation (use of "not" operator)
        
#not TRUE = FALSE
#not FALSE = TRUE

def y():
    x = input("Number: ")
    #Empty variables/inputs are False (0)
    #while not False ==>
        #while True ==> Loop carries on
    #Compound condition
        #Simple condition + logical operator
    while not x:
        x = input("Number: ")
    #while not True ==>
        #while False ==> Loop stops
    
#y()
        
#-------------------------------------------------------------------------

#Forgetfull While (Use of "continue" operator)
        
def inf():        
    chosen = int(input("Number to skip: "))        
    count = 0
    while True:
        #This produces an "intentional infinite loop"
        count += 1
        #End loop if count greater than 10
        if count > 10:
            break
        #Skips the inputed number
        if count == chosen:
            continue
            #continue statement means "jump back to the
            #top of the loop"
        #Prints "count"
        print(count)
#inf()

#-------------------------------------------------------------------------
 
#Eh close enough (Use of the "or" operator)

#With the "or" operator, if one condition is True, then
#both conditions will be True.
#TRUE and FALSE = TRUE
        
def orr():
    
    
    username = input("Username: ")
    while not username:
        username = input("Username: ")
    
    password = input("Password: ")
    while not password:
        password = input("Password: ")
        
    if username == "hello" or password == "world":
        print("\nEh close enough.")
        print("Access Granted")
    else:
        print("\nNope")
        print("Access denied")
        
#orr()

#-------------------------------------------------------------------------

#Please specify (Use of "and" operator)

#With the "and" operator, both conditions must be True in
#order to have an overall True condition
#TRUE and FALSE = FALSE
#TRUE and TRUE = TRUE
        
def andd():
    
    username = input("Username: ")
    while not username:
        username = input("Username: ")
    
    password = input("Password: ")
    while not password:
        password = input("Password: ")
        
    if username == "hello" and password == "world":
        print("\nAccess Granted")
    else:
        print("\nNope")
        print("Access denied")
    
#andd()
