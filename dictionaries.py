# [Infinite-Program] Dictionary: Name & Age
#Experimentation with dictionaries and program efficiency
  
def func(dictionary):
    return dictionary.get(str(input("Name: ")).lower(),"\nName not in database")
print("Age:",func({"james":22, "bob":33}))

