myDict = {
    "fast": "In A Quick Manner",
    "harry": "A Coder",
    "marks" : [1 ,5 ,7],
    "anotherdict": {'shanu': 'player'},
    1:2
}

#Dictionary Method
print(list(myDict.keys())) #print the keys of the dictionary
print(myDict.values()) ##print the values of the dictionary
print(myDict.items()) #print the (key,value) for all the contents of the dictionary
print(myDict)
updateDic = {
    "lavish": 'Friend',
    "shanu": 'Friend',
    "shaheer": 'Friend', 
    "harry": 'Dancer'       ##update harry
}
myDict.update(updateDic)  #update the dictionary by adding key-value pairs from updateDict
print(myDict)

print(myDict.get("harry")) # --> print value assiociated with "harry"
print(myDict["harry"])     # --> print value assiociated with "harry"

# Difference b/w .get and [] syntax in dictionary?
print(myDict.get("harry2")) #-->print None as harry2 is not present in dictionary
#print(myDict["harry2"])    -->throws Error as harry2 is not present in dictionary

