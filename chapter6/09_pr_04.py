#find whether a given username contains less than 10 characters or not

from operator import index


Username = input("Enter your name:\n")
if (len(Username) < 10):
    print("This username have less than 10 character")
else:
    print("This username have more than 10 character")