#find first sum of natural num

num = int(input("enter number"))
if num<0:
    print("write posite number")

else:
    k = 1
    while num>0:
        k += num    #---> k = k + num
        num -= 1    #---> num = num - 1
    print("the sum is",k)
