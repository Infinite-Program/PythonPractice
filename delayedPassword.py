#Made by Infinite-Program
import time

#Simple Password program
counter01 = 0
counter = 0
passw = input("Password: ")
    #Sentry Variable
while passw != "world":
    counter01 += 1
    print("Access Denied")
    if counter01 >= 3:
        counter += 1
        timer = counter*60
        print("Please try again in {0} seconds.".format(timer))
        time.sleep(timer)
    passw = input("Password: ")
print("Access Granted")



    



