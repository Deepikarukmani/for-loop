#python pattern programs
 #looping knowledge (nested loop)
for i in range(5):
    print("* "*4)

#While (nested loop):
row=1
while row<=5:
    for i in range(5):
        print(row, end=" ")
    print()
    row += 1


#For(nested loop):
for row in range(6):
    for i in range(5):
        print(row, end=" ")
    print()

# for loop nested to find reverse
for row in range(6):
    for col in range(5,0,-1):
        print(col,end=" ")
    print

# for loop nested to find reverse
for row in range(5,0,-1):
    for col in range(5,0,-1):
        print(row, end="")
    print()

#increase to decrease program:
for row in range(6,1, -1):
    for col in range(1,row):
        print(col, end=" ")
    print()

#increase to decrease program:
row=5
while row>=1:
    for col in range(row):
        print(1, end=" ")
    print()
    row -= 1


#increase to decrease program:
row=5
no=1
while row>=1:
    for col in range(row):
        print(no, end=" ")
    print()
    row -= 1
    no=no+1