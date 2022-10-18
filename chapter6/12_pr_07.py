# write a program to find out whether a given post is taking about "harry" or not

a = "harry" and "Harry"
post = input("Enter your post:\n")

if a in post:
    print("this post include name harry")
else:
    print("this post have not name harry")