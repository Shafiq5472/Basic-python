#pattern
n = 3
for i in range (3):
    print(" " * (n-i-1),end="")
    print("*" * (2*i+1),end="")
    print(" " * (n-i-1))


# for i in range(0, n):
#     for j in range(n-i-1):
#         print(" ",end=" ")
#         for k in  range(0, i+1):
#             print("*", end=" ")
# print()
