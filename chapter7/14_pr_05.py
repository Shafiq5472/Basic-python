#n! = 1 X 2 X 3.....X n


num = int(input("Enter your number"))
k = 1
for i in range(1,num+1):
    k = k * i
print(f"The factorial of {num} is {k}")