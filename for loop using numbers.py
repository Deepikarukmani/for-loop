To find table using for loop
no= 1
for num in range(4, 41, 4):
    print(no, "* 4 =", num)
    no+=1

To find factorial using for loop
no = 5
factorial = 1
for i in range(1, no+1):
    factorial = factorial*1
else:
    print(factorial)

To find prime number using for loop
no = int(input("enter number"))
for div in range(2, no):
    if no%div==0:
        print("not prime")
        break
else:
    print("prime")

To find reverse word using for loop
word = "deepi"
for i in range(len(word)-1,-1,-1):
    print(word[i], end= " ")
