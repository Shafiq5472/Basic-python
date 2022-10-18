#print multiplication table of a given number using for loop

num = int(input("Enter your number:\n"))
for i in range(1,11):
    #print(str(num) + 'X' + str(i) + '=' + str(i*num))
    print(f"{num}X{i}={num*i}")

#%%
num = int(input("Enter your number:\n"))
i=0
while i<=10:
    print(f"{num}X{i}={num*i}")
    i=i+1