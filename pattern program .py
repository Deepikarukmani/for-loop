# pattern program 1 to 5
a = int(input())
for col in range(1, 6):
        print("* " * col, end=" ")
        print()

# pattern program 1 to 15
a = int(input())

for row in range(1, 16):
    for col in range(row, 16):
        print(col, end=" ")
    print()

# pattern program * output
n= int(input())
for i in range(n+1):
    print("* " * i)
    print()