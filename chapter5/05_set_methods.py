# creating an empty set
b = set()
print(type(b))

#Adding value in empty set
b.add(4)
b.add(5)
b.add(3)
b.add(5) #--> same value doesn't change the set
#b.add([4,5,6]) #list can't add
b.add((5,4,7,2)) #tupel add bcz tuple can't change
#b.add({"shanu": "Good",
    # "shafiq": "handsome"}) --> also don't add dictionary
print(b)

#lenght of a set
print(len(b))

#remove from a set
b.remove(5)
#b.remove(15) #throws an error bcz 15 is not in set
print(b)

#remove any thing from set
print(b.pop())
print(b)


