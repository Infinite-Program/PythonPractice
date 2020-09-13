# [Infinite-Program] Dictionary: Name & Age 
    #Adding/Replacing Key-Value pair:
        #dictionary[key] = value
#Delet Key-Value pair:
    #del dictionry[key]

def func(dictionary,name = str(input("Name: ")).lower(),age = int(input("Age: "))):
    if name not in dictionary:
        dictionary[name] = age
    else:
        return "\nName already exists"
    return dictionary.get(str(input("\nName: ")).lower(),"\nName not in database")
print("Age:",func({"james":22, "bob":33}))

    
    

