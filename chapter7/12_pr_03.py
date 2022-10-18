#find whether a given num is prime or not

num = int(input("Enter the number \n"))
prime = True
for i in range(2,num):
    if(num%i ==0):
        prime = False
        break
if prime:
    print(f"{num} is prime")
else:
    print("This number is NOT prime")


print("even")
for j in range(1, 10):
    if(j % 2 == 0):
        print(j)

print("odd")
for number in range(1, 10):
    if(number % 2 != 0):
        print(number)