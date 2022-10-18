rows = 5
b = 0
# reverse for loop from 5 to 0
for i in range(rows, 0, -1):
    b += 1
    for j in range(1, i + 1):
        print(b, end=' ')
    print('')

''' i = 5,4,3,2,1

for i = 5
b=0+1=1
        j=1,2,3,4,5
for j=1
"print(b)" 1
for j=2
again 1
so
1 1 1 1 1

for i=4
b=2
j=1,2,3,4
2 2 2 2 
and so on......
'''