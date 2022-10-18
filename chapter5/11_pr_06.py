'''Create an empty dictionary. Allow 4 friend to enter thier fvrt language as value 
and use key as thier names. Assume that the name are unique'''


favLang = {}
a=input("Enter your favourite LANGUAGE Shanu\n")
b=input("Enter your favourite LANGUAGE Shaheer\n")
c=input("Enter your favourite LANGUAGE ibrahim\n")
d=input("Enter your favourite LANGUAGE sanaullah\n")

favLang['shanu'] = a 
favLang['Shaheer'] = b
favLang['ibrahim'] = c
favLang['sanaullah'] = d

print(favLang)

#%%

#if the name of 2 friend are same; What will happen to the program in problem 6

favLang = {}
a=input("Enter your favourite LANGUAGE Shanu\n")
b=input("Enter your favourite LANGUAGE Shaheer\n")
c=input("Enter your favourite LANGUAGE ibrahim\n")
d=input("Enter your favourite LANGUAGE sanaullah\n")

favLang['shanu'] = a 
favLang['Shaheer'] = b
favLang['shanu'] = c
favLang['sanaullah'] = d

print(favLang)


#%%


# %%

#if the language of 2 friend are same?

favLang = {}
a=input("Enter your favourite LANGUAGE Shanu\n")
b=input("Enter your favourite LANGUAGE Shaheer\n")
c=input("Enter your favourite LANGUAGE ibrahim\n")
d=input("Enter your favourite LANGUAGE sanaullah\n")

favLang['shanu'] = a 
favLang['Shaheer'] = b
favLang['ibrahim'] = c
favLang['sanaullah'] = d

print(favLang)
