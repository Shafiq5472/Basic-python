'''Create a dictionary of urdu words with values as their english translation.
 Provide user with an option to look it up'''

myDict = { "pankha" : "fan",
    "tasweer" : "pic",
    "gharrri" : "clock"
}
print("Option are", myDict.keys())
a = input("Enter the urdu word \n")
print("The meaning of word is :", myDict[a])
