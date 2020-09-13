#Program created by Jacob Shkeir
#Dice Roll Game project

def accountMechanism():
    print("""
0 - Exit
1 - Sign in
2 - Sign up

""")
    #Sign in and sign up mechanism
    op = ""
    fh = open("myData.txt","a")
    fh.close
    while op != "0":
        op = str(input("Option: "))
        print("")
        #Sign in option:
        if op == "1":
            print("Sign in selected")
            print("")
            print("User 1")
            username01 = input("Username: ")
            password01 = input("Password: ")
            print("")
            print("User 2")
            username02 = input("Username: ")
            password02 = input("Password: ")
            print("")
            with open("myData.txt","r") as file:
                blank = " "
                blank = file.readline()
                dataList = blank.split()
                #Checks if credentials are correct
                if username01 and password01 and username02 and password02 in dataList:
                    if username01 != username02:
                        print("Identification confirmed")
                        import random
                        from random import randint
                        import time

                        def welcomeMessages():
                            #Welcome messages and introduction to the game
                            print("\nWelcome to The Lucky Dice game\n")
                            time.sleep(0.25)

                            print("How it works:\n")
                            time.sleep(0.25)
                            
                            print("You will each get to roll two six sided die and will get")
                            print("points depending on what you roll. There are five rounds and in")
                            print("each round, you and your opponent will roll the two dice.")
                            print("You may choose amongst yourselves who will be Player 1 and")
                            print("who will be Player 2.\n")
                            time.sleep(0.25)

                            print("Rules:\n")
                            time.sleep(0.25)
                            print("The total of your dice roll will be added to your score.")
                            print("You score will not go bellow zero at any point.")
                            print("If the total of your roll is an even number, an additional 10 points")
                            print("will be added to your score. However, if the total of your roll is")
                            print("an odd number, then 5 points will be subtracted form your score.")
                            print("If you are really lucky and roll a double, you get to roll one extra die")
                            print("and you will get the result of the roll added to your score.")
                            print("If you have the highest score at the end of the five rounds,")
                            print("then you win! However if you do not have the highest score at")
                            print("the end of the five rounds then you loose.")
                            print("Additionally if you have the same score as your opponent at the end")
                            print("of the five rounds, then you each get to roll one die untill one of")
                            print("you get a higher score than the other.")
                            time.sleep(4)
                            print("Lets begin...\n\n")
                            time.sleep(0.25)


                        def gameMechanism():
                            #Starting scores initialised
                            scoreP1 = 0
                            scoreP2 = 0

                            for i in range(5):
                                #Roll variables
                                p1Roll1 = random.randint(1,6)
                                p1Roll2 = random.randint(1,6)
                                p1DoubleRoll = random.randint(1,6)
                                
                                p2Roll1 = random.randint(1,6)
                                p2Roll2 = random.randint(1,6)
                                p2DoubleRoll = random.randint(1,6)

                                #Player 1 turn:
                                print("{0} will roll".format(username01))
                                input("Press enter to roll")
                                print("You rolled {0} and {1}".format(p1Roll1,p1Roll2))
                                p1Sum = p1Roll1 + p1Roll2
                                
                                #Odd and even outcomes:
                                if (p1Sum%2) == 0:
                                    scoreP1 += p1Sum
                                    scoreP1 += 10
                                else:
                                    scoreP1 -= 5
                                if scoreP1 < 0:
                                    scoreP1 += 5
                                    
                                #If the player rolls a double:
                                if p1Roll1 == p1Roll2:
                                    print("You rolled a double!")
                                    print("You get to roll one extra die.")
                                    input("Press enter to roll again.")
                                    print("You rolled {0}".format(p1DoubleRoll))
                                    scoreP1 += p1DoubleRoll
                                print("Your score has been updated.")
                                print("{0} score: {1}\n".format(username01,scoreP1))

                                #Player 2 turn:
                                print("{0} will roll".format(username02))
                                input("Press enter to roll")
                                print("You rolled {0} and {1}".format(p2Roll1,p2Roll2))
                                p2Sum = p2Roll1 + p2Roll2
                                
                                #Odd and even outcomes:
                                if (p2Sum%2) == 0:
                                    scoreP2 += p2Sum
                                    scoreP2 += 10
                                else:
                                    scoreP2 -= 5
                                if scoreP2 < 0:
                                    scoreP2 += 5
                                    
                                #If the player rolls a double:
                                if p2Roll1 == p2Roll2:
                                    print("You rolled a double!")
                                    print("You get to roll one extra die.")
                                    input("Press enter to roll again.")
                                    print("You rolled {0}".format(p2DoubleRoll))
                                    scoreP2 += p2DoubleRoll
                                print("You score has been updated.")
                                print("{0} score: {1}\n".format(username02,scoreP2))
                                
                            #If both players have the same score at the end:
                            while scoreP1 == scoreP2:
                                p1Roll = random.randint(1,6)
                                p2Roll = random.randint(1,6)
                                print("You both have the same score!")
                                print("You will each roll one die untill we have a winner.\n")

                                print("{0} will roll".format(username01))
                                input("Press enter to roll")
                                print("You rolled {0}\n".format(p1Roll))

                                print("{0} will now roll".format(username02))
                                input("Press eneter to roll")
                                print("You rolled {0}\n".format(p2Roll))
                            
                                #Variable values are finalised
                                scoreP1 += p1Roll
                                scoreP2 += p2Roll
                            
                            if scoreP1 > scoreP2:
                                print("{0} has won!".format(username01))
                                print("Good game.")
                                
                            else:
                                print("{0} has won!".format(username02))
                                print("Good game.")
                                 
                        welcomeMessages()
                        gameMechanism()

                        break
                    else:
                        print("You can not both sign in using the same accounts.")
                        print("Please make sure that both users use different accounts.\n")
                else:
                    print("Access denied")
                    print("Username or password is incorrect.\n")
            
        #Sign up option    
        if op == "2":
            print("Sign up selected")
            username = input("Username: ")
            password = input("Password: ")
            with open("myData.txt","r") as file02:
                blank = " "
                blank = file02.readline()
                dataList = blank.split()
                #Checks if the username has been taken
                if username not in dataList:
                    print("")
                    with open("myData.txt","a") as file:
                        file.write(" ")
                        file.write(username)
                        file.write(" ")
                        file.write(password)
                        print("Account has been created\n")
                else:
                    print("")
                    print("The username '{0}' is already taken".format(username))
                    print("Please choose an alternative username\n")
    #Exit option
    else:
        print("Good bye")

accountMechanism()