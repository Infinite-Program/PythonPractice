#WHILE LOOPS

"""
NOTE:

- Must update the sentry variable to avoid an infitite loop whilst using a "while" loop
- Conditions in a "while" loop must always eventually evaluate to FALSE in order
  for the loop to stop
- FALSE can also be represented by 0 or no input
- Any other value is TRUE, even negatives

"""
#------------------------------------------------------------------------------------

def mainHero():
    
    import time

    try: 

        #Constants are represented in Caps
        HEALTH = 10
        trolls = 0
        DAMAGE = 2

        print("Hero has {0} health\n".format(HEALTH))

        while HEALTH > 0:
            trolls += 1
            HEALTH -= DAMAGE

            print("Hero defeats a troll")
            print("Hero takes {0} damage\n".format(DAMAGE))
            time.sleep(0.8)
            print("Hero has {0} life points remaining".format(HEALTH))

            if HEALTH <= 0:
                print("Your hero has died")
                    
    except Exception as error:
        print("You have come across an errorr")
        print(error)
                
        
mainHero()

#--------------------------------------------------------------------------------------

def test01():

    #The loop has to evaluate to False but if it is not then it will keep on running
    #In other words, you will get an infinite loop
    
    #False = 0
    #True = Any other input other than 0 (for example 1)

    while True :
        #Infinite loop
        #Value is never == to False
        
        print("Hi")

#test01()

#--------------------------------------------------------------------------------------

import time

def test02():

    print("To eneter the database please log in...\n")

    #Set the sentry variable
    #Since username is initialised to the empty string
    #in the program, it starts out as False
    username = ""

    #While not False which is the same as While True
    #This means it will keep on running untill the
    #sentry variable is updated which makes it True
    #That means the statement then turns into While not True
    #which is the same as while False.
    #This then ends the loop and moves on.

    while not username:
        username = input("Username: ")

    password =  ""

    while not password:
        password = input("Password: ")

    if username == "admin" and password == "admin":
        print("Granted")
        
    else:
        print("Incorrect credentials")

#test02()


#---------------------------------------------------------------------------------------

#Input verification program

def inputVef():

    #Sets the sentry variable
    name = ""
    #The variable "name" is false because it
    #has nothings assigned to it

    while not name:
        #Same as while True because not is opposite
        name = input("Name: ")
        
        #This program will kepp running untill the
        #sentry variable is updated to True which will make
        #the whole condition while not True which is the same
        #as while False, this will end the loop

#inputVef()
        
    