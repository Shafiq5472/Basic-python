rows = 6
for i in range(rows):
#for i in range(1,rows) --> skip space line
    for j in range(i):
        print(i, end=' ')
    print('')


  
''' for i = 0,1,2,3,4,5
for i=0
j=0
None

for i = 1
j = 0
1
 
for i = 2
j = 0,1
for j=0
(2 )
for j=1
(2 )(2 )

for i = 3
j=0,1,2
for j=0
(3 )
for j=1
(3 )(3 )
for j=2
(3 )(3 )(3 ) and so on..
'''